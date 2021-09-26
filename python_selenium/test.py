from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to give search of differentr key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#selenium documentation https://selenium-python.readthedocs.io/
import time
PATH ="C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)


driver.get("https://techwithtim.net")
print(driver.title) #to get title of website

search = driver.find_element_by_name("s")
search.send_keys("test") #send test in search of website
search.send_keys(Keys.RETURN) #OR USE ENTER

# print(driver.page_source) # source code of page
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")))

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
except:

    driver.quit()



time.sleep(5)
driver.close() #to close tab of the website
driver.quit() #to quit browser
