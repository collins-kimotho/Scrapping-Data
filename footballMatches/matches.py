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

time.sleep(5)

driver.quit()