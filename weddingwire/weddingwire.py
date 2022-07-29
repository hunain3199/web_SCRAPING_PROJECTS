from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('https://www.weddingwire.com/shared/search?group_id=1&state_id=427&page=1')
# links = driver.find_elements_by_xpath("//div[@class='vendorTile__content']/h2/a")
# for i in links:
#     with open('links.csv', 'a', newline='') as f_object:
#         writer_object = writer(f_object)
#         writer_object.writerow([i.get_attribute('href')])
#         f_object.close()
#
# next_btn = driver.find_element_by_xpath("//span[@class='pagination__next']/button")
# next_btn.click()
#
# flag = True
# while flag:
#     try:
#         links = driver.find_elements_by_xpath("//div[@class='vendorTile__content']/h2/a")
#         for i in links:
#             with open('links.csv', 'a', newline='') as f_object:
#                 writer_object = writer(f_object)
#                 writer_object.writerow([i.get_attribute('href')])
#                 f_object.close()
#
#         time.sleep(2)
#         next_btn = driver.find_element_by_xpath("//span[@class='pagination__next']/button")
#         next_btn.click()
#         time.sleep(3)
#
#
#     except:
#         flag = False

for i in range(1,45):
    with open('links.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(['https://www.weddingwire.com/shared/search?group_id=1&state_id=427&page='+str(i)])
        f_object.close()

