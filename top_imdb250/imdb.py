#!/usr/bin/env python3  
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/top/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
response.raise_for_status()

# print(response)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
# Find all movies
all_movies = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 iyTDQy compact-list-view ipc-metadata-list--base').find_all('li', class_='ipc-metadata-list-summary-item sc-4929eaf6-0 DLYcv cli-parent' )

# print(len(all_movies))

# print(movies.text)
data = []
for movie in all_movies:
    dic = {}
    dic['Title'] = movie.find('h3', class_='ipc-title__text').text.split('.')[1]
    dic['Year'] = movie.find('div', class_='sc-300a8231-6 dBUjvq cli-title-metadata').find('span', class_='sc-300a8231-7 eaXxft cli-title-metadata-item').text.strip('')
    dic['Rating'] = movie.find('span', class_='ipc-rating-star--rating').text

    

    data.append(dic)

# print(data)
df = pd.DataFrame(data)

df.to_excel('IMDbTop250Movies.xlsx', index=False)
df.to_csv('IMDbTop250Movies.csv', index=False)




   

