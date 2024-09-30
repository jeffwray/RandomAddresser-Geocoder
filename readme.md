# RandomAddresser-Geocoder

RandomAddresser-Geocoder is a Python project that merges multiple CSV files containing address data and geocodes the addresses using the Google Geocoding API. The geocoded addresses are then saved to a new CSV file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/RandomAddresser-Geocoder.git
    cd RandomAddresser-Geocoder
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file by copying the `.env.example` file and filling in your actual values:

    ```sh
    cp .env.example .env
    ```

## Usage

1. Load the CSV files captured from RandomAddresser into the main directory.

2. Merge CSV files:

    ```sh
    python merge_csv.py
    ```

    These CSV files should be generated using the Chrome extension at https://github.com/jeffwray/RandomAddresser. This will merge all CSV files in the current directory into a single file specified by `INPUT_FILE` in your `.env` file.

3. Geocode addresses:

    ```sh
    python google_geocode.py
    ```

    This will geocode the addresses in the merged CSV file and save the results to the file specified by `OUTPUT_FILE` in your `.env` file.

## Configuration

The project uses a `.env` file to manage configuration variables. The following variables need to be set:

- `GOOGLE_API_KEY`: Your Google Geocoding API key.
- `INPUT_FILE`: The name of the merged CSV file containing addresses.
- `OUTPUT_FILE`: The name of the output CSV file to save geocoded addresses.
- `MAX_CHUNKS`: The maximum number of chunks to process (optional).

Example `.env` file:


## License

(C) 2024 BIGDEALIO, LLC.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for research and non-commercial purposes, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
The Software shall not be used for commercial purposes without explicit permission from the authors.
The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the Software.
