#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for i in range (1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    res = requests.get(url)
    res.raise_for_status()
    # print(res)
    soup = BeautifulSoup(res.content, 'html.parser')
    # print(soup.prettify())

    books = soup.find('ol', class_='row').find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    # print(books)

    for book in books:
        title = book.find('h3').find('a')['title']
        rating = book.find('p').attrs['class'][1]
        price = book.find('div', class_='product_price').find('p', class_='price_color').text.replace("£", "")
        availability = book.find('div', class_='product_price').find('p', class_='instock availability').text.strip()

        all_books.append({
            'title': title,
            'rating': rating,
            'price': price,
            'availability': availability
        })

df = pd.DataFrame(all_books)
df.to_csv('books.csv', index=False)
df.to_excel('books.xlsx', index=False)
