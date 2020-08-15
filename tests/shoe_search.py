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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nike.com/")

# create variable to store search term
search_term = "Nike Air Force 1 '07"

# read config.json file
with open('./config.json') as f:
    data = json.load(f)


# search item
def search():
    driver.implicitly_wait(10)  # 10 is in seconds
    searchTextBox = driver.find_element_by_id("TypeaheadSearchInput")
    searchTextBox.send_keys(search_term)
    driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav[1]/section[2]/div/div[3]/div[1]/div/div/div/button[2]").click()


# filter search options
def filter():
    e = data["product_info"]["product_name"]
    if data["product_info"]["W/M"] == "M":
        men_selector = driver.find_element_by_xpath("//*[@id='wallNavFG0']/button[1]/span")
        driver.implicitly_wait(1)
        men_selector.click()
    else:
        women_selector = driver.find_element_by_xpath("//*[@id='wallNavFG0']/button[2]/div/div")
        driver.implicitly_wait(1)
        women_selector.click()


# click on item
def click_item():
    d = data["product_info"]["product_name"]
    if search_term == data["product_info"]["product_name"]:
        print("valid searched item")
        if data["product_info"]["W/M"] == "W":
            print("women's shoe")
            women_item = driver.find_element_by_xpath("//div[contains(@class, 'product-card__subtitle') and text()='Women\'s Shoe']")
            driver.implicitly_wait(1)
            women_item.click()
        else:
            print("men's shoes")
            men_item = driver.find_element_by_xpath("//div[contains(@class, 'product-card__subtitle') and text()='Men\'s Shoe']")

            driver.implicitly_wait(1)
            men_item(1)

# women shoe size selection
def women_shoes():
    a = data["product_info"]["W/M"]
    if a == 'W':
        print("women's shoe")
        if int(float(data["product_info"]["size"])) == 5:
            print("size 5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[1]/label").click()
        elif int(float(data["product_info"]["size"])) == 5.5:
            print("size 5.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[2]/label").click()
        elif int(float(data["product_info"]["size"])) == 6:
            print("size 6")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[3]/label").click()
        elif int(float(data["product_info"]["size"])) == 6.5:
            print("size 6.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[4]/label").click()
        elif int(float(data["product_info"]["size"])) == 7:
            print("size 7")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[5]/label").click()
        elif int(float(data["product_info"]["size"])) == 7.5:
            print("size 7.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[6]/label").click()
        elif int(float(data["product_info"]["size"])) == 8:
            print("size 8")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[7]/label").click()
        elif int(float(data["product_info"]["size"])) == 8.5:
            print("size 8.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[7]/label").click()
        elif int(float(data["product_info"]["size"])) == 9:
            print("size 9")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[9]/label").click()
        elif int(float(data["product_info"]["size"])) == 9.5:
            print("size 9.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[10]/label").click()
        elif int(float(data["product_info"]["size"])) == 10:
            print("size 10")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[11]/label").click()
        elif int(float(data["product_info"]["size"])) == 10.5:
            print("size 10.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[12]/label").click()
        elif int(float(data["product_info"]["size"])) == 11:
            print("size 11")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[13]/label").click()
        elif int(float(data["product_info"]["size"])) == 11.5:
            print("size 11.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[14]/label").click()
        elif int(float(data["product_info"]["size"])) == 12:
            print("size 12")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[15]/label").click()
        else:
            raise Exception("Invalid Size")


# men shoe size selection
def men_shoes():
    b = data["product_info"]["W/M"]
    if b == 'M':
        print("men's shoe")
        if int(float(data["product_info"]["size"])) == 3.5:
            print("size 3.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[1]/label").click()
        elif int(float(data["product_info"]["size"])) == 4:
            print("size 4")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[2]/label").click()
        elif int(float(data["product_info"]["size"])) == 4.5:
            print("size 4.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[3]/label").click()
        elif int(float(data["product_info"]["size"])) == 5:
            print("size 5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[4]/label").click()
        elif int(float(data["product_info"]["size"])) == 5.5:
            print("size 5.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[5]/label").click()
        elif int(float(data["product_info"]["size"])) == 6:
            print("size 6")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[6]/label").click()
        elif int(float(data["product_info"]["size"])) == 6.5:
            print("size 6.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[7]/label").click()
        elif int(float(data["product_info"]["size"])) == 7:
            print("size 7")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[9]/label").click()
        elif int(float(data["product_info"]["size"])) == 7.5:
            print("size 7.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[10]/label").click()
        elif int(float(data["product_info"]["size"])) == 8:
            print("size 8")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[11]/label").click()
        elif int(float(data["product_info"]["size"])) == 8.5:
            print("size 8.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[12]/label").click()
        elif int(float(data["product_info"]["size"])) == 9:
            print("size 9")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[13]/label").click()
        elif int(float(data["product_info"]["size"])) == 9.5:
            print("size 9.5")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[14]/label").click()
        elif int(float(data["product_info"]["size"])) == 10:
            print("size 10")
            driver.implicitly_wait(1)
            driver.find_element_by_xpath("//*[@id='buyTools']/div[1]/fieldset/div/div[15]/label").click()
        else:
            raise Exception("Invalid Size")


# automate M / W  and  size selection
def user_info():
    try:
        women_shoes()
    except ValueError:
        print("User data is invalid")
    else:
        men_shoes()

    # add shoe to cart


# add to cart
def add_to_cart():
    cart = driver.find_element_by_css_selector(
        "#floating-atc-wrapper > div > button.ncss-btn-primary-dark.btn-lg.css-y0myut.add-to-cart-btn")
    driver.implicitly_wait(1)
    cart.click()
    cart.click()


# checkout
def checkout():
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(
        "//*[@id='PDP']/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/div/button[2]").click()


# Member login
def member_login():
    searchEmailTextBox = driver.find_element_by_css_selector("input[type='email']")
    searchEmailTextBox.send_keys(data["member_acct"]["email"])
    searchPasswordTextBox = driver.find_element_by_css_selector("input[type='password']")
    searchPasswordTextBox.send_keys(data["member_acct"]["password"])
    driver.find_element_by_css_selector("input[value='MEMBER CHECKOUT']").click()


# authorization of login
def authorization():
    # try to comment out driver text to see if assertion error will work
    driver.find_element_by_xpath('//*[@id="app-container"]/div[1]/div/div[3]/div').click()
    try:
        assert "CHECKOUT" in driver.title
    except AssertionError:
        print("Invalid sign in credentials")


# call each function
def automate():
    search()
    filter()
    click_item()
    user_info()
    add_to_cart()
    checkout()
    member_login()
    authorization()


automate()
