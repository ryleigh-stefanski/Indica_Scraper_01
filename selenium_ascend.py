import web_scraping_selenium_functions as funcs

import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

#return i = -1 if element found
def check_for_element(driver, search_key, max_elements_checked):
    items = driver.find_elements(By.CSS_SELECTOR, '[class="sc-35f5af31-0 eGRdab"]')
    num = 0;
    for i in items:
        print("Checking %s / %s items..." % (num, len(items)))
        ele = i.get_attribute("innerHTML")
        if(ele.find(search_key) != -1):
            print("Found at %s" % num)
            return True
        else:
            num += 1
    return False

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

def sel_ascend_run(search_key, url, max_scrolls_to_bottom,max_elements_checked,wait_for_load_time):
    driver = open_web_driver(url)
    bypass_age_check(driver)
    traverse_page(driver, max_scrolls_to_bottom, wait_for_load_time)
    found = check_for_element(driver, search_key, max_elements_checked)	
    driver.close()
    return found
    
#sel_ascend_run("Kitchen Sink", "https://letsascend.com/menu/pa-scranton-menu-med/categories/flower", 30, 300, .15)