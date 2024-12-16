# Scraping Gross domestic product (GDP) at basic prices, by industry, quarterly average 

This project scrapes data from the Statistics Canada website(https://www.statcan.gc.ca/en/start) using Selenium and BeautifulSoup, and processes it into a pandas DataFrame.

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/collins-kimotho/Scrapping-Data.git
    cd canadaStats
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the [stats.py](stats.py) script:
    ```sh
    python stats.py
    ```

2. The script will scrape data from the Statistics Canada website and print the resulting DataFrame.


## Notes

- The script sets an implicit wait time of 10 seconds and uses `time.sleep` to wait for specific elements to load.

## License

This project is licensed under the MIT License.
