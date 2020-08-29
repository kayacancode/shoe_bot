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
def filter_m_w():
    e = data["product_info"]["W/M"]
    if e == "M":
        men_selector = driver.find_element_by_xpath("//*[@id='wallNavFG0']/button[1]/span")
        driver.implicitly_wait(1)
        men_selector.click()
    else:
        women_selector = driver.find_element_by_xpath("//*[@id='wallNavFG0']/button[2]/div/div")
        driver.implicitly_wait(1)
        women_selector.click()
"""
Function filter color would not work because NIKE changes the color positions  each time 

"""
def filter_color():
    c = data["product_info"]["Colorway"]
    if c == "White/White":
        print("Shown: White/White")
        white_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[8]/div")
        driver.implicitly_wait(1)
        white_selector.click()
    elif c == "Black/Back":
        print("Shown:Black/Black")
        black_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[1]/div/div")
        driver.implicitly_wait(1)
        black_selector.click()
    elif c == "Blue/Blue":
        print("Shown: Blue/Blue")
        blue_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[2]/div/div")
        driver.implicitly_wait(1)
        blue_selector.click()
    elif c == "Red/Red":
        print("Shown: Red/Red")
        red_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[7]/div/div")
        driver.implicitly_wait(1)
        red_selector.click()
    elif c == "Brown/Brown":
        print("Shown: Brown/Brown")
        brown_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[3]/div/div")
        driver.implicitly_wait(1)
        brown_selector.click()
    elif c == "Green/Green":
        print("Shown: Green/Green")
        green_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[3]/div/div")
        driver.implicitly_wait(1)
        green_selector.click()
    elif c == "Grey/Grey":
        print("Shown: Grey/Grey")
        grey_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[4]/div/div")
        driver.implicitly_wait(1)
        grey_selector.click()
    elif c == "Orange/Orange":
        print("Shown: Orange/Orange")
        orange_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[5]/div/div")
        driver.implicitly_wait(1)
        orange_selector.click()
    elif c == "Yellow/Yellow":
        print("Shown: Yellow/Yellow")
        yellow_selector = driver.find_element_by_xpath("//*[@id='wallNavFG2']/button[10]/div/div")
        driver.implicitly_wait(1)
        yellow_selector.click()
    else:
        print("Invalid Color")
"""
---*Penny for my thoughts*-----
        -ENTRY|8/15/20 | shoes for example the NIKE Airforce 1's are a vague topic
        no way with selenium could we factor that one shoe 
        maybe in the JSON file we would need to add more parameters 
        for example like search for certain scraping api that gets shoes from websites 
        so on the web app people will have more parameters to select a certain shoe / color way/ size
        then the automation code could be tailored for those specific types of shoes instead of one specific shoe 
        with the more parameters we could use the filter capability that NIKE provides 
        the question is how to do that with other sites although i am pretty sure that all ecommerce websites have
        that capability for examples filter on the left side of page to get a more specific type of shoe| 8/16/20
        -ENTRY| 8/16/20 |Colorway in JSON file it is required to have two words in both sections for example 
        for a blue pair of shoes blue/blue , for a white pair of shoes white/white , for a red and black shoe
         red/black .look how ecommerce sites place there different colors ways |
        NIKE:
            - Shown: White/White
            - Shown: Black/Black 
            - Shown: Pure Platinum/White/Hyper Crimson/Indigo Fog
        we might have to scrap colors ways from webpage. also we could put price of shoe in JSON config files
        -Another way to handle data is in the functions require an argument to make it more specific.
        You can pull the argument data from the JSON file
"""


# click on item
def click_item():
    d = data["product_info"]["product_name"]
    if search_term == d:
        print("valid searched item")
        men_item = driver.find_element_by_xpath("//div[@class='product-card__subtitle' and  contains(., \"Men's "
                                                "Shoe\")]")
        women_item = driver.find_element_by_xpath("//div[@class='product-card__subtitle' and contains(., "
                                                  "\"Women's Shoe\")]")
        m = data["product_info"]["W/M"]
        if m == men_item:
            print("Men's Shoe")
            WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable((By.CLASS_NAME, "product-card__subtitle")))
            men_item.click()
        else:
            print("Women's Shoe")
            WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable((By.CLASS_NAME, "product-card__subtitle")))
            women_item.click()
        # if data["product_info"]["W/M"] == "W":
        #     print("women's shoe")
        #     women_item = driver.find_element_by_xpath("//div[@class='product-card__subtitle' and contains(., "
        #                                               "\"Women's Shoe\")]")
        #     driver.implicitly_wait(1)
        #     women_item.click()
        # else:
        #     print("men's shoes")
        #     men_item = driver.find_element_by_xpath("//div[@class='product-card__subtitle' and  contains(., \"Men's "
        #                                             "Shoe\")]")
        #
        #     men_item.click()  # not working because the click is intercepted by the img


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
    filter_m_w()
    filter_color()
    click_item()
    user_info()
    add_to_cart()
    checkout()
    member_login()
    authorization()


automate()
