#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')
# print(len(rows))

countries_list = []

for row in rows:
    data = {}

    data['Country'] = row.find_all('td')[1].text
    data['Population'] = row.find_all('td')[2].text.replace(',','')

    countries_list.append(data)

df = pd.DataFrame(countries_list)
df.to_excel('world_population.xlsx', index=False)
df.to_csv('world_population.csv', index=False)

print(df.head())

      