import web_scraping_selenium_functions as funcs

import re
import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

#extract price, size, and brand
def extract_element_values(ele):
    pr, si, br = "N/A"
    price = re.findall(r"\$[0-9]?[0-9]?[0-9]\.?[0-9]?[0-9]?", ele)
    if price:
        pr = price[0]
        
    size = re.findall(r"[1-9]/[1-9] oz", ele)
    if size:
        si = size[0]
        
   # brand = re.findall(r'<div class="sc-35f5af31-0 cduLoD">(.+)' ,ele)
    #if brand:
     #   br = brand[0][0:brand[0].find('</div>')] #cuts at first div marker
    
    return pr, si, br

#searches the items list for all items in the search_key list
def search_page_elements(search_key, items):
    found_items = []
    pos = 0
    for key in search_key:
        for i in items:
            print("Checking %s / %s items on this page for key %s..." % (pos, len(items), key))
            ele = i.get_attribute("innerHTML")
            if(ele.find(key) != -1):
                print("Found")
                found_items.append((key, extract_element_values(ele)))
            else:
               pos += 1
    return found_items
    
def search_page(driver, search_key): 
    funcs.scroll_to_bottom(driver, 1)
        
    #check for element
    try:
        items = driver.find_elements(By.CSS_SELECTOR, '[class="desktop-product-list-item__Container-sc-8wto4u-0 jTzrhU"]')
    except:
        print("Could not retreive elements...")
        return []
    return search_page_elements(search_key, items)

def next_page(driver):
    print("Moving to next page...")
    try:
        driver.find_element(By.CSS_SELECTOR, '[class="pagination-controls__NavButton-sc-1436mnk-1 hjQwsb"]').click()
    except:
        print("Could not move to next page...")
        return -1
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

#returns items as such
#found_items[i] where i = page number
#found_items[0][j] where j is the element on that certain page
#found_items(name, [0][0][0-3])where 0 = strain name, 1= price, 2= size, 3 = brand
def traverse_pages(driver, search_key):
    found_items = []
    page_number = 1
    while True:
        found = (search_page(driver, search_key))
        if found:
            found_items.append(found)
        stop = next_page(driver)
        if stop == -1:
            return found_items
        page_number += 1
        if page_number > 5:
            break 
    return found_items

def sel_ethos_run(search_key, url):    
    driver = open_web_driver(url)
    bypass_age_check(driver)
    found = traverse_pages(driver, search_key)
    driver.close()
    return found

#sel_ethos_run(["Tahoe Apple", "Sled Dog", "Perfect Cell", "CannaConfusion"], "https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower")