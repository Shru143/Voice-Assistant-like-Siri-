from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class infow():
    def __init__(self):
        # Add your ChromeDriver path if required
        self.driver = webdriver.Chrome(service=Service())

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        
        # Wait for the search input field to become visible
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]')))
        
        # Search for the query
        search.click()
        search.send_keys(query)
        
        enter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button')))
        enter.click()

        # Adding time delay for you to see the page load (optional)
        time.sleep(15)
