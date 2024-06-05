import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

#scrolls to the bottom of the webpage using the END key
def scroll_to_bottom(driver, wait_for_load_time):
	elem = driver.find_element(By.TAG_NAME, "html")
	elem.send_keys(Keys.END)
	time.sleep(wait_for_load_time)
   