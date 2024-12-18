from bs4 import BeautifulSoup
import requests
import time

root = 'https://subslikescript.com/'
url = f'{root}/movies'

res = requests.get(url)
content = res.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    url = f'{root}/{link}'
    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w') as f:
        f.write(transcript)
