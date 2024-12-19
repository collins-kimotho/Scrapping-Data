from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

url = 'https://cullenjewellery.com/engagement-rings'

# Set up the Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()
driver.maximize_window()

# Load the webpage
driver.get(url)

try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "load-more")]'))
    )
    driver.execute_script("arguments[0].click();", button)
except Exception as e:
    print(f'Cannot find button: {e}')

container = driver.find_element(By.XPATH, '//ul[@class = "root Thumbs svelte-d2ewq4"]')
rings = container.find_elements(By.TAG_NAME, 'li')
print(len(rings))


time.sleep(10)
driver.quit()