# Audible Bestsellers Scraper

This project is a web scraper for extracting information about best-selling audiobooks from Audible. The scraper navigates through multiple pages of bestsellers, collects data about each book, and saves the data to a CSV file.

## Features

- Scrapes book titles, authors, lengths, and ratings from Audible's bestsellers list.
- Handles pagination to scrape data from multiple pages.
- Saves the collected data to a CSV file.

## Requirements

- Python 3.12 or higher
- Google Chrome browser
- ChromeDriver
- Selenium
- Pandas

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/audible-bestsellers-scraper.git
    cd audible-bestsellers-scraper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download ChromeDriver and place it in your project directory. Ensure that the version of ChromeDriver matches your installed version of Google Chrome.

## Usage

1. Clone the repository
    ```sh
    git clone https://github.com/collins-kimotho/Scrapping-Data.git
    cd audible
    ```
2. Create a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

4. Run the scraper:
    ```sh
    python audible.py
    ```

2. The scraper will navigate through multiple pages of bestsellers and save the collected data to `bestSellers.csv` and `bestSellers.xlsx`.

## Code Explanation

The main script [audible.py](audible.py) performs the following steps:

1. Sets up Selenium WebDriver with necessary options for headless browsing.
2. Navigates to the Audible bestsellers page.
3. Handles pagination to scrape data from multiple pages.
4. Extracts book titles, authors, lengths, and ratings.
5. Saves the collected data to CSV and excel files.

### Handling Pagination

The script identifies the pagination elements and iterates through each page by clicking the "Next" button until the last page is reached.

### Error Handling

The script includes error handling to manage cases where elements are not found or pages fail to load.

## Example Output

The output CSV file `books.csv` will have the following columns:

- Title
- Author
- Length
- Rating

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

