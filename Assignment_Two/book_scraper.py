from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()




"""
Scrape books from All products | Books to Scrape - Sandbox
(Book name, price, stock status (in stock or out of stock), rating, description, product information, category (poetry, fiction, historical fiction, etc)

Scrape the first 5 pages (20 books per page)

Scrape 10-20 distinct quote authors from Quotes to Scrape
(Name, nationality, description, date of birth)

Build a scraper that will scrape a random page from Wikipedia
"""

PATH_TO_DRIVER = os.getenv('PATH_TO_DRIVER')
#  set up the drivers and web browsers
URL = 'https://books.toscrape.com/'

service = Service(
    executable_path=PATH_TO_DRIVER)
DRIVER = webdriver.Chrome(service=service)
DRIVER.maximize_window()
DRIVER.get(URL)
time.sleep(3)
DRIVER.implicitly_wait(10020)
BOOK_DATA = []

for i in range(5):
    try:
        print('page', i)

        def getBookList():
            BOOK_WEB_SITE = DRIVER.find_element(By.TAG_NAME, 'ol')
            LISTS = BOOK_WEB_SITE.find_elements(By.TAG_NAME, 'li')
            return LISTS

        LISTS = getBookList()
        print('Len of Books in Current Page', len(LISTS))

        def loopThroughBookList(LISTS):
                for i in range(len(LISTS)):
                    try:
                        # DRIVER.implicitly_wait()
                        CLICKABLE_IMAGE = LISTS[i].find_element(
                            By.CLASS_NAME, 'image_container').find_element(By.TAG_NAME, 'a')
                        CLICKABLE_IMAGE.click()
                        time.sleep(3)
                        # Get data from the book details page
                        CATEGORIES = DRIVER.find_element(By.CLASS_NAME, 'breadcrumb').find_elements(
                            By.TAG_NAME, 'li')[2].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML').strip()
                        # print(CATEGORIES)
                        PRODUCT_PAGE = DRIVER.find_element(
                            By.CLASS_NAME, 'product_page')
                        PRODUCT_DETAILS_COLLECTION = PRODUCT_PAGE.find_element(
                            By.CLASS_NAME, 'product_main')
                        BOOK_NAME = PRODUCT_DETAILS_COLLECTION.find_element(
                            By.TAG_NAME, 'h1').get_attribute('innerHTML').strip()
                        # print(BOOK_NAME)
                        P_TAGS_IN = PRODUCT_DETAILS_COLLECTION.find_elements(
                            By.TAG_NAME, 'P')
                        BOOK_PRICE = P_TAGS_IN[0].get_attribute('innerHTML').strip()
                        # print(BOOK_PRICE)
                        BOOK_IN_STOCK = P_TAGS_IN[1].get_attribute(
                            'innerHTML').split('>')[-1].strip()
                        # print(BOOK_IN_STOCK)
                        BOOK_RATING = P_TAGS_IN[2].get_attribute('class').strip()
                        # print(BOOK_RATING)
                        DESCRIPTION = PRODUCT_PAGE.find_elements(
                            By.TAG_NAME, 'p')[3].get_attribute('innerHTML').strip()
                        # print("Desc",DESCRIPTION)
                        print('\n\n')
                        TABLE = PRODUCT_PAGE.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME,'tr')
                        DATA = {
                            'BookName': BOOK_NAME,
                            'Price':BOOK_PRICE,
                            'Rating':BOOK_RATING,
                            'In_Stock':BOOK_IN_STOCK,
                            'Description':DESCRIPTION,
                            'Category':CATEGORIES,
                        }
                        for i in range(len(TABLE)):
                            TH = TABLE[i].find_element(By.TAG_NAME,'th').get_attribute('innerHTML').strip()    
                            TD = TABLE[i].find_element(By.TAG_NAME, 'td').get_attribute('innerHTML').strip()
                            DATA[f'{TH}'] = TD
                        print(DATA)
                        BOOK_DATA.append(DATA)
                        DRIVER.back()
                    except Exception as e: 
                        print('Error From Inner Loop',e)
                        continue

        loopThroughBookList(LISTS)
        # go to next page after the loop is done

        NEXT_BUTTON = DRIVER.find_element(By.CLASS_NAME, 'pager').find_element(
            By.CLASS_NAME, 'next').find_element(By.TAG_NAME, 'a')
        NEXT_BUTTON.click()
        time.sleep(20)
    except Exception as e: 
        print('Error Form Outer Loop',e)
        continue

with open('BookData.json','w') as File: 
    File.write(json.dumps(BOOK_DATA))