#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# Create an instance of Options
options = Options()

# Add options
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

# Set an implicit wait time
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610044901'
driver.get(url)

# Wait for a specific element to load (example: wait for 5 seconds)
time.sleep(5)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

prices = soup.find('table', id='simpleTable').find('tbody', id='simpleTableBody').find_all('tr', class_='highlight-row')

print(len(prices))

all_prices = []

for price in prices:
    industries = price.find('th').text
    quarters = price.find_all('td', class_='align-right nowrap')
    quarters = [int(q.text.replace(',', '')) for q in quarters]
    all_prices.append([industries] + quarters)

# Define column names
columns = ['Industry', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']

# Create DataFrame
df = pd.DataFrame(all_prices, columns=columns)
df.to_csv('prices.csv', index=False)
df.to_excel('prices.xlsx', index=False)

# print(df)
# Close the browser
driver.quit()