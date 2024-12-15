# Book Scraper

This project is a web scraper that extracts information about books from a book catalog website (https://books.toscrape.com/) and stores it in a CSV file. The extracted information includes the title, rating, price, and availability of each book.

## Project Structure

- `books.csv`: The CSV file where the scraped book data is stored.
- `books.py`: The main script that performs the web scraping.
- `books.xlsx`: The Excel file where the scraped book data is stored.
- `requirements.txt`: The file listing the dependencies required for the project.
- `venv/`: The virtual environment directory.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/collins-kimotho/Scrapping-Data.git
    cd books_scrape
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
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

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the [books.py](http://_vscodecontentref_/4) script to scrape the book data:
    ```sh
    python books.py
    ```

2. The scraped data will be saved in [books.csv](http://_vscodecontentref_/5) and [books.xlsx](http://_vscodecontentref_/6).

## Dependencies

The project requires the following Python packages:
- pandas
- beautifulsoup4
- requests

These dependencies are listed in the [requirements.txt](http://_vscodecontentref_/7) file.

## License

This project is licensed under the MIT License.