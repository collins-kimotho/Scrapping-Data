from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-extensions')



url = 'https://www.audible.com/adblbestsellers?ref_pageloadid=not_applicable&pf_rd_p=bb0efe44-14ef-41cc-91b0-c1b40e66ffe2&pf_rd_r=VREK12VSR80T5AYCEQEF&plink=WsS0pxxk43B4hWXF&pageLoadId=4vbmwiQcy4XOY7Ec&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482&ref=a_search_t1_navTop_pl0cg1c0r0'
# path = '/home/optimus/Desktop/chromedriver'

# service = Service(path)
driver = webdriver.Chrome( options=options)
driver.get(url)

# Pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')

last_page = int(pages[-2].text)

current_page = 1
    

lib = []
while current_page <= last_page:
    try:
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container "))
        )
        all_books = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')
    except Exception as e:
        print(f"Books not found {e}...")
    


    for book in all_books:
        try:
            title = book.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
            author = book.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text.replace("By:", "").strip()
            length = book.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text.replace("Length:", "").strip()
            try:
                rating = book.find_element(By.XPATH, './/li[contains(@class, "ratingsLabel")]/span[2]').text.replace("ratings", "")
            except:
                rating = "Not rated yet"
            lib.append({
                'Title': title,
                'Author': author,
                'Length': length,
                'Rating': rating,
            })
        except Exception as e:
            print(f"-----------An error has occurred while fetching books: {e}------")

    
    current_page += 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
        time.sleep(5)
    except Exception as e:
        print(f'Next page not found: {e}')
    
    

driver.quit()

df = pd.DataFrame(lib)
df.to_csv('bestSellers.csv', index=False)
df.to_excel('bestSellers.xlsx', index=False)