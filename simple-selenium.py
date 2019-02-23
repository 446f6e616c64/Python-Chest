#!/usr/bin/env python3

'''
This script is a simple Selenium script that automates the process of 
opens a Firefox browser, goes to Zillow.com, enters
a zipcode (Hardcoded at this time) and then hits the Enter key.
@446f6e616c64 - 23FEB2019
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.zillow.com/homes")
assert "Zillow" in driver.title

elem = driver.find_element_by_name("citystatezip")
elem.clear()
elem.send_keys("20176")
elem.send_keys(Keys.RETURN)

# driver.close()
