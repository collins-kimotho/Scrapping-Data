# Movie Transcripts Scraper

This project scrapes movie transcripts from the website `subslikescript.com` and saves them as text files.

The code goes through all the links in the `home/movies' section, proceeds to save the links in a list then opens each link to find the transcript of each movie.


## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` library

You can install the required libraries using the following command:

```sh
pip install requests beautifulsoup4 lxml
```
## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` library

You can install the required libraries using the following command:

```sh
pip install requests beautifulsoup4 lxml
```

Create a virtual environment and activate it.

Run the `movies.py` script to scrape the transcripts:
```
python movies.py
```

The script will download the transcripts and save them as text files in the current directory.