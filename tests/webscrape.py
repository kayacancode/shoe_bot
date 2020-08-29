from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import json
import requests
import re
import time
import os
import wget

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

def download_image(url):
    image_name = url.split("/")[-1]
    destination = "assets/" + image_name
    if os.path.exists(destination):
        return True
    wget.download(url, destination)

def get_items(search,page):
    search = search.replace(" ", "_")
    url = "https://www.nike.com/w/mens-nike-air-force-1-5sj3yz7yfbznik1?q=nike%20air%20force%201s".format(
        search, page
    )
    driver.get(url)
    # sleep for a second then scroll to the bottom of the page
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    items = driver.find_element_by_class_name("product-grid css-14yqij9")
    output = []

    for i in items:
        try:
            price = i.find_element_by_class_name("product-price css-11s12ax is--current-price").text
        except:
            price = None
        try:
            name = i.find_element_by_class_name("product-card__title").text
        except:
            name = None
        try:
            product_url = i.find_element_by_css_selector("a").get_attribute("href")
        except:
            product_url = None
        try:
            product_image =

