from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import time
import pandas as pd
import csv
from csv import writer


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.pakwheels.com/used-cars/search/-/")



# flag =True
# while flag:
#     links = []
#     link = driver.find_elements_by_xpath("//a[@class = 'car-name ad-detail-path']")
#     for i in link:
#
#         print(i.get_attribute('href'))
#         button = driver.find_element_by_xpath("//a[@rel='next']")
#         button.click()
#     flag =False







# link = driver.find_elements_by_xpath("//a[@class = 'car-name ad-detail-path']")
# for i in link:
#     link_s = []
#     link_s.append(i.get_attribute('href'))
#     print(link_s)

# link_s = []
# link = driver.find_elements_by_xpath("//a[@class = 'car-name ad-detail-path']")
# flag = True
# for i in link:
#     try:
#         link_s.append(i.get_attribute('href'))
#         print(link_s)
#         while flag:
#
#             try:
#
#                 button = driver.find_element_by_xpath("//a[@rel='next']")
#                 button.click()
#                 driver.implicitly_wait(10)
#
#
#
#
#             except:
#
#                 flag = False
#     except:
#         pass
# 1st page links


# detail = driver.find_elements_by_xpath("//div[@class ='search-title']/a")
# for i in detail:
#     with open('decided.csv', 'a', newline='') as f_object:
#         writer_object = writer(f_object)
#         writer_object.writerow([i.get_attribute('href')])
#         f_object.close()
# # Pagination Links
#     # Pagination Links
# button = driver.find_element_by_xpath("//button[@class = 'close']")
# flag = True
#
# while flag:
#     try:
#         btn = driver.find_element_by_xpath("//a[@rel = 'next']")
#         btn.click()
#         ActionChains(driver).move_to_element(button).click(button).perform()
#         driver.implicitly_wait(10)
#
#         for i in detail:
#             with open('decided.csv', 'a', newline='') as f_object:
#                 writer_object = writer(f_object)
#                 writer_object.writerow([i.get_attribute('href')])
#                 f_object.close()
#
#
#     except:
#         flag = False
#         pass

#
btn = driver.find_element_by_xpath("//button[@class = 'align-right primary slidedown-button']")
btn.click()
driver.implicitly_wait(10)


flag = True
while flag:
    details = driver.find_elements_by_xpath("//a[@class = 'car-name ad-detail-path']")
    for i in details:
        with open('decided.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([i.get_attribute('href')])
            f_object.close()

    try:
        btn = driver.find_element_by_xpath("//a[@class = 'next']")
        btn.click()
        driver.implicitly_wait(10) # seconds
        # details = driver.find_elements_by_xpath("//a[@class = 'car-name ad-detail-path']")

        # for i in details:
        #     with open('decided.csv', 'a', newline='') as f_object:
        #         writer_object = writer(f_object)
        #         writer_object.writerow([i.get_attribute('href')])
        #         f_object.close()

    except:
        flag = False
        break








