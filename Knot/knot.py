from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import time
import pandas as pd
import csv
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('https://www.theknot.com/marketplace/wedding-reception-venues-windham-me?sort=featured')
# driver.implicitly_wait(10)
# def scrap():
#     links = driver.find_elements_by_xpath("//a[@class='info-container--87e97']")
#     for i in links:
#         with open('links.csv', 'a', newline='') as f_object:
#             writer_object = writer(f_object)
#             writer_object.writerow([i.get_attribute('href')])
#             f_object.close()
#     next_btn = driver.find_element_by_xpath("(//a[@class='clickableArea--ff112'])[3]")
#     next_btn.click()
#     driver.implicitly_wait(10)
#
#     flag = True
#     while flag:
#         try:
#             links = driver.find_elements_by_xpath("//a[@class='info-container--87e97']")
#             for i in links:
#                 with open('links.csv', 'a', newline='') as f_object:
#                     writer_object = writer(f_object)
#                     writer_object.writerow([i.get_attribute('href')])
#                     f_object.close()
#
#             next_btn = driver.find_element_by_xpath("(//a[@class='clickableArea--ff112'])[3]")
#             next_btn.click()
#             driver.implicitly_wait(10)
#
#
#         except:
#             flag = False
def scraping():
    link_list = ['https://www.theknot.com/marketplace/wedding-reception-venues-windham-me?sort=featured',
                 'https://www.theknot.com/marketplace/wedding-reception-venues-windham-me?page=2&sort=featured',
                 'https://www.theknot.com/marketplace/wedding-reception-venues-windham-me?page=3&sort=featured']
    for i in link_list:
        driver.get(i)
        links = driver.find_elements_by_xpath("//a[@class='info-container--87e97']")
        for i in links:
            with open('links.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([i.get_attribute('href')])
                f_object.close()
        time.sleep(3)

scraping()