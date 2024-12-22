# Audible Spider

This project is a web scraping tool built using Scrapy to extract data from the Audible website. The spider scrapes audiobook information, including titles, authors, and lengths, and handles pagination to scrape multiple pages.


## Project Structure

```
audibleSpider/
├── audibleSpider/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── audible.py
└── run.sh
```

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/collins-kimotho/Scrapping-Data.git
    cd audibleSpider/audibleSpider/audibleSpider/spiders/audible.py
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run the spider:**
    ```bash
    scrapy crawl audible
    ```
    You can also use the bash file created to run the script
    ```bash
    ./run.sh
    ```

## Scraped Data

The spider extracts the following information from each audiobook listing on Audible:
- **Title**
- **Author**
- **Length**

## Pagination Handling

The spider is designed to handle pagination and will automatically follow the "next" page links to scrape data from multiple pages. In this project, we successfully scraped data from 25 pages of the Audible website.

## Output

The scraped data is yielded in a structured format and can be further processed or stored as needed. Run the commands;
```bash
./run.sh -o <filename.csv> # To store as csv
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
