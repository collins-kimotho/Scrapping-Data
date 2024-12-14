import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://cullenjewellery.com/engagement-rings'

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Load the webpage
driver.get(url)
time.sleep(5)  # Wait for the JavaScript to load

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

rings = soup.find('div', class_='results flex column limit-width svelte-128ewnv').find('ul', class_='root Thumbs svelte-d2ewq4').find_all('li', class_='root disable-user-select Thumb svelte-19gl59f interactive')

ring_data = []

for ring in rings:
    dic = {}
    dic['name'] = ring.find('div', class_='description svelte-19gl59f').find('h2', class_='svelte-19gl59f').text
    dic['price'] = ring.find('div', class_='price svelte-19gl59f').text.replace('STARTING', "").replace('USD', "").replace(",","").strip()
    ring_data.append(dic)

df = pd.DataFrame(ring_data)
df.to_csv('ring_data.csv', index=False)  # Save the DataFrame to a CSV file
df.to_excel('ring_data.xlsx', index=False)  # Save the DataFrame to an Excel file

print("Data saved to ring_data.csv and ring_data.xlsx")