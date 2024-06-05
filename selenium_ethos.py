import web_scraping_selenium_functions as funcs

import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

def search_page(driver, search_key):   
    funcs.scroll_to_bottom(driver, 1)
        
    #check for element
    items = driver.find_elements(By.CSS_SELECTOR, '[class="desktop-product-list-item__ProductName-sc-8wto4u-7 kjymBK"]')

    pos = 0
    for i in items:
        print("Checking %s / %s items on this page..." % (pos, len(items)))
        ele = i.get_attribute("innerHTML")
        if(ele.find(search_key) != -1):
            print("Found")
            return True
        else:
           pos += 1
    return False

def next_page(driver):
    print("Moving to next page...")
    driver.find_element(By.CSS_SELECTOR, '[class="pagination-controls__NavButton-sc-1436mnk-1 hjQwsb"]').click()
    time.sleep(1)

#selenium bypass age check
def open_web_driver(url):
    try:
        print("Accessing Webpage Via Selenium...")
        driver = webdriver.Chrome()
        driver.get(url)
    except:
        print("Failed to open web driver...")
    return driver

def bypass_age_check(driver):
    try:
        print("Bypassing Age Check...")
        #"//button[@data-testid='age-restriction-yes'
        driver.find_element(By.CSS_SELECTOR, '[data-testid="age-restriction-yes"]').click()
    except:
        print("Failed to bypass age check...")

def traverse_pages(driver, search_key):
    found = False
    page_number = 1
    while(found == False):
        found = search_page(driver, search_key)
        next_page(driver)
        page_number += 1
        if page_number > 5:
            return False  
    return True

def sel_ethos_run(search_key, url):    
    driver = open_web_driver(url)
    bypass_age_check(driver)
    found = traverse_pages(driver, search_key)
    driver.close()
    return found

#sel_ethos_run("Gello", "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower")