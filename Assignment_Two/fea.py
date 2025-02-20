from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from d import list_product
load_dotenv()


PATH_TO_DRIVER = os.getenv('PATH_TO_DRIVER')
#  set up the drivers and web browsers
URL = 'https://www.pinterest.com/ideas/'

service = Service(
    executable_path=PATH_TO_DRIVER)
DRIVER = webdriver.Chrome(service=service)
DRIVER.maximize_window()
DRIVER.get(URL)
time.sleep(3)
DRIVER.implicitly_wait(10020)

for i in range(len(list_product)):
    SearchInput = DRIVER.find_element(By.NAME, 'searchBoxInput')
    # Input text into the search bar
    SearchInput.send_keys(list_product[i]['name'])

    # Optionally, submit the form (if needed)
    SearchInput.send_keys(Keys.RETURN)
    time.sleep(10)
    DRIVER.back()




