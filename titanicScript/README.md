# Titanic Script Scraper

This project scrapes the full transcript of the movie "Titanic" from the website [subslikescript.com](subslikescript.com) and saves it to a text file.

## Requirements

- Python 3.12
- `requests` library
- `beautifulsoup4` library

## Setup

1. Clone the repository or download the script.
2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
4. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python titanic.py
    ```
2. The script will scrape the transcript from the specified URL and save it to a text file named `Titanic.txt`.

## Files

- [titanic.py](titanic.py): The main script that performs the web scraping.
- [requirements.txt](requirements.txt): Lists the required Python libraries.

