from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




url = 'https://www.audible.com/search'
path = '/home/optimus/Desktop/chromedriver'

service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container "))
    )
    all_books = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')
except Exception as e:
    print(f"Book not found {e}...")
   

lib = []

for book in all_books:
    try:
        title = book.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
        author = book.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text.replace("By:", "").strip()
        length = book.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text.replace("Length:", "").strip()
        rating = book.find_element(By.XPATH, './/li[contains(@class,	"ratingsLabel")]').text[0]
        print(rating)
    except Exception as e:
        print(f"-----------An error has occurred while fetching books: {e}------")

driver.quit()