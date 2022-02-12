from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from csv import writer

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.yell.com/k/popular+searches.html?api_key=1fbee64eeded0cb9cdcbd33ad4c21dc6&url=http://httpbin.org/ip")

option = driver.find_elements_by_xpath("//div[@class= 'findLinks--item']/a")
# options=[]
for i in option:
    # options.append(i.get_attribute('href'))
    # print(options)

    with open('options.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([i.get_attribute('href')])
        f_object.close()
