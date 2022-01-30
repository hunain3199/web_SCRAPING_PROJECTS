from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import time
import pandas as pd
import csv
from PagesData import pagesData
from csv import writer

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://pa1.swindon.gov.uk/publicaccess/search.do?action=monthlyList')


option = driver.find_elements_by_xpath("//select[@id = 'month']//option")
options = []
for i in option:
    options.append(i.text)
print(options)

driver.close()





for i in options:
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get('https://pa1.swindon.gov.uk/publicaccess/search.do?action=monthlyList')

        select = driver.find_element_by_xpath("//select[@id='month']")
        select.click()
        driver.implicitly_wait(10)  # seconds


        typeSelect = driver.find_element_by_xpath(f"(//input[@name = 'dateType'])[2]")
        typeSelect.click()

        if i == driver.find_element_by_xpath(f"//select[@id = 'month']/option[text()='{i}']").text:
            driver.find_element_by_xpath(f"//select[@id = 'month']/option[text()='{i}']").click()

            driver.implicitly_wait(10)
            search = driver.find_element_by_xpath("//input[@class ='button primary recaptcha-submit']").click()

            # 1st page links
            driver.implicitly_wait(10)
            details = driver.find_elements_by_xpath("//li[@class ='searchresult']//a")
            for i in details:
                with open('decided.csv', 'a', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([i.get_attribute('href')])
                    f_object.close()

            # Pagination Links
            flag = True
            while flag:
                try:
                    btn = driver.find_element_by_xpath("//a[@class = 'next']")
                    btn.click()
                    driver.implicitly_wait(10) # seconds
                    details = driver.find_elements_by_xpath("//li[@class ='searchresult']//a")

                    for i in details:
                        with open('decided.csv', 'a', newline='') as f_object:
                            writer_object = writer(f_object)
                            writer_object.writerow([i.get_attribute('href')])
                            f_object.close()

                except:
                    driver.close()
                    flag = False




    except:
        break



pagesData('decided.csv','decided_summary.csv' ,'decided_further.csv','decided_contact.csv','decided_date.csv','decided_constraint.csv','decided_document.csv')
