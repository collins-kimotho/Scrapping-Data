# Football Matches Scraping

This project scrapes football match data from the website [Adam Choi's Football Matches](https://www.adamchoi.co.uk/overs/detailed) and saves it into a CSV file.
For this project we scrape data from all matches in the Spain league. We achieve this by using selenium and chromedriver to select the Spain league and click on all matches. We then identify the tables with matches and save them into a csv and excel file.

## Prerequisites

- Python 3.12
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/collins-kimotho/Scrapping-Data.git
    cd footballMatches
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the ChromeDriver and place it in the project directory. Make sure it is executable:
    ```sh
    chmod +x chromedriver
    ```

## Usage

1. Run the script:
    ```sh
    python matches.py
    ```

2. The script will scrape the data and save it into a CSV file named [matches.csv](matches.csv) and an excel file named [matches.xlsx](matches.xlsx).




