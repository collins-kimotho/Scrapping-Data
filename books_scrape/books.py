#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd


for i in range (1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    res = requests.get(url)
    res.raise_for_status()
    print(res)

    
