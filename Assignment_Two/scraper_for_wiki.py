from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()

PATH_TO_DRIVER = os.getenv('PATH_TO_DRIVER')

URL = 'https://en.wikipedia.org/wiki/Cold_War'
SERVICE = Service(
    executable_path=PATH_TO_DRIVER)
DRIVER = webdriver.Chrome(service=SERVICE)
print('driver')
DRIVER.maximize_window()
DRIVER.get(URL)
time.sleep(3)
DRIVER.implicitly_wait(10020)


action = ActionChains(DRIVER)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(3)

copied_text = pyperclip.paste()

with open('wiki_text.txt', 'w', encoding='utf-8') as file:
    file.write(copied_text.strip())

DRIVER.quit()
