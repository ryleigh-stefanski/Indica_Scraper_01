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
    
    #selenium bypass age check
def open_web_driver(url):
    try:
        print("Accessing Webpage Via Selenium...")
        driver = webdriver.Chrome()
        driver.get(url)
    except:
        print("Failed to open web driver...")
    return driver

#will throw an exception if it reaches the bottom of the page
def load_all_results(driver, number_of_scrolls):
        while(number_of_scrolls > 0):
            driver.find_element(By.CSS_SELECTOR, '[name="Load More"]').click()
            number_of_scrolls -= 1

#searches the items list for all items in the search_key list
def search_page_elements(search_key, items):
    found_items = []
    for key in search_key:
        pos = 0
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
    items = []
    for strain in search_key:
        try:
            items = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
        except:
            print("Could not find elements...")
            return []
    return search_page_elements(search_key, items)       
 
def sel_beyondh_run(search_key, url):    
    driver = open_web_driver(url)
    time.sleep(4)
    try:
        load_all_results(driver, 4)
    except:
        print("Could not load more results...")
    found = search_page(driver, search_key)
    driver.close()
    return found

#print(sel_beyondh_run(["Tahoe Apple"], "https://www.iheartjane.com/embed/stores/1639/menu?filters%5Broot_types%5D%5B%5D=flower"))
