import web_scraping_selenium_functions as funcs

import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#extract price, size, and brand
def extract_element_values(ele):
    pr, si, br = "N/A"
    price = re.findall(r"\$[0-9]?[0-9]?[0-9]\.?[0-9]?[0-9]?", ele)
    if price:
        pr = price[0]
        
    size = re.findall(r"[0-9]?[0-9].?[0-9][0-9]?g", ele)
    if size:
        si = size[0]
        
    brand = re.findall(r'<div class="sc-35f5af31-0 cduLoD">(.+)' ,ele)
    if brand:
        br = brand[0][0:brand[0].find('</div>')] #cuts at first div marker
    
    return pr, si, br

#return i = -1 if element found
#returns a list of items matching the name
#list elements look like this [search_key, (price, size, brand)]
def check_for_element(driver, search_key, max_elements_checked):
    return_items = []
    items = driver.find_elements(By.CSS_SELECTOR, '[class="sc-6ef47149-0 hVgJPP"]')
    num = 0;
    for i in items:
        print("Checking %s / %s items..." % (num, len(items)))
        ele = i.get_attribute("innerHTML")
        if(ele.find(search_key) != -1):
            print("Found at %s" % num)
            return_items.append(extract_element_values(ele))
        else:
            num += 1
    return return_items

def traverse_page(driver, max_scrolls_to_bottom, wait_for_load_time):
    #load all elements
    refreshes = max_scrolls_to_bottom

    while(refreshes > 0):
        print("Accessing webpage %s / %s..." % (max_scrolls_to_bottom - refreshes, max_scrolls_to_bottom))
        funcs.scroll_to_bottom(driver, wait_for_load_time)
        refreshes -= 1

def bypass_age_check(driver):
    #bypass age check
    try:
        print("Bypassing Age Check...")
        driver.find_element(By.CSS_SELECTOR, '[class="sc-80be13e8-4 WlTEr"]').click()
    except:
        print("Failed")

def open_web_driver(url):
    try:
        print("Accessing Webpage Via Selenium...")
        driver = webdriver.Chrome()
        driver.get(url)
        assert "medical Flower" in driver.title
    except:
        print("Failed")
    return driver

#if found returns {found status},  price, size, and brand
def sel_ascend_run(search_key, url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time):
    returned_items = []

    driver = open_web_driver(url)
    bypass_age_check(driver)
    traverse_page(driver, max_scrolls_to_bottom, wait_for_load_time)
    i = 0
    while i < len(search_key):
        returned_items.append(check_for_element(driver, search_key[i], max_elements_checked))
        i += 1
    driver.close()
    return returned_items
    
#print(sel_ascend_run(["Cream", "Jupiter #3"], "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower", 30, 300, .1))