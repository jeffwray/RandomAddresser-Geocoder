import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def merge_csv_files(input_directory, output_file):
    # List to hold dataframes
    dataframes = []

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_directory, filename)
            # Read the CSV file into a dataframe
            df = pd.read_csv(file_path)
            dataframes.append(df)

    # Concatenate all dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Write the merged dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_directory = "."  # Current directory
    output_file = os.getenv("INPUT_FILE")  # Desired output file name
    merge_csv_files(input_directory, output_file)
