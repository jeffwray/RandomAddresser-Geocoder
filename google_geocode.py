import pandas as pd
import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def geocode_address(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

def geocode_csv(input_file, output_file, api_key, chunk_size=100, max_chunks=None):
    df = pd.read_csv(input_file)
    
    # Check if the output file already exists
    if os.path.exists(output_file):
        df_output = pd.read_csv(output_file)
        processed_indices = set(df_output.index)
    else:
        df_output = pd.DataFrame(columns=df.columns.tolist() + ['Latitude', 'Longitude'])
        processed_indices = set()

    latitudes = []
    longitudes = []
    chunks_processed = 0

    for index, row in df.iterrows():
        if index in processed_indices:
            continue

        address = f"{row['Address']}, {row['State']}, {row['Zip']}"
        lat, lng = geocode_address(address, api_key)
        latitudes.append(lat)
        longitudes.append(lng)
        processed_indices.add(index)

        # Append the new data to the output dataframe
        new_row = pd.DataFrame({
            **row,
            'Latitude': lat,
            'Longitude': lng
        }, index=[index])
        df_output = pd.concat([df_output, new_row])

        # Save the output file every chunk_size rows
        if len(latitudes) >= chunk_size:
            df_output.to_csv(output_file, index=False)
            latitudes = []
            longitudes = []
            chunks_processed += 1
            print(f"Processed {chunks_processed * chunk_size} addresses...")

            # Stop if max_chunks is reached
            if max_chunks and chunks_processed >= max_chunks:
                print(f"Reached the maximum of {max_chunks} chunks. Stopping.")
                return

            time.sleep(0.1)  # To avoid hitting the rate limit

    # Save any remaining rows
    if latitudes:
        df_output.to_csv(output_file, index=False)
        print(f"Processed {chunks_processed * chunk_size + len(latitudes)} addresses in total.")

if __name__ == "__main__":
    input_file = os.getenv("INPUT_FILE")
    output_file = os.getenv("OUTPUT_FILE")
    api_key = os.getenv("GOOGLE_API_KEY")
    max_chunks = int(os.getenv("MAX_CHUNKS", 500))
    geocode_csv(input_file, output_file, api_key, max_chunks=max_chunks)
