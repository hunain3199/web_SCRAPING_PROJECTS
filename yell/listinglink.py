from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
# options =webdriver.ChromeOptions()
# options.add_argument("--window-size =1100,1000")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get("https://www.yell.com/k/popular+searches.html?api_key=1fbee64eeded0cb9cdcbd33ad4c21dc6&url=http://httpbin.org/ip")
#
# times = random.randint(5,10)
# time.sleep(times)
import csv
from csv import writer

driver = webdriver.Chrome(executable_path='chromedriver.exe')
with open('sublinks.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            print(i)

            driver.get(i)
            time.sleep(2)
            # list_links=driver.find_elements_by_xpath("//a[@class ='businessCapsule--title']")
            # for j in list_links:
            #     with open('listing.csv', 'a', newline='') as f_object:
            #         writer_object = writer(f_object)
            #         writer_object.writerow([j.get_attribute('href')])
            #         f_object.close()
            #         flag = True
            #         while flag:
            #             try:
            #                 driver.find_element_by_xpath("//a[@class = 'btn btn-blue btn-fullWidth pagination--next']").click()
            #                 driver.implicitly_wait(10)
            #                 list_links = driver.find_elements_by_xpath("//a[@class ='businessCapsule--title']")
            #                 for j in list_links:
            #                     with open('listing.csv', 'a', newline='') as f_object:
            #                         writer_object = writer(f_object)
            #                         writer_object.writerow([j.get_attribute('href')])
            #                         f_object.close()
            #             except:
            #                 flag = False
            #
            #







