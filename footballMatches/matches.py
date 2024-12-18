from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/home/optimus/Desktop/chromedriver'

service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get(url)

try:
    dropdown = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    select = Select(dropdown)
    select.select_by_visible_text('Spain')
except Exception as e:
    print(f"An error occurred: {e}")

try:
    all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
    all_matches_button.click()
except Exception as e:
    print(f"Button not clicked: {e}")

# Wait for the tables to load
time.sleep(3)

try:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    print(len(rows))
except Exception as e:
    print(f"An error has occured while fetching rows: {e}")
time.sleep(10)

driver.quit()