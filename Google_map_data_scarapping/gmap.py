from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time
import string
import openpyxl
import os

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 5)

#Opening Google maps
driver.get("https://www.google.com/maps")
time.sleep(3)
