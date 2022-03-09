from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
import csv
from csv import writer

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window() # For maximizing window
with open('product_links.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:

            driver.get(i)
            time.sleep(2)

            try:
                company = driver.find_element_by_xpath("//h3[@class='mt1kvu ka2E9k uMhVZi FxZV-M SZKKsK pVrzNP _5Yd-hZ']").text

            except Exception as e:
                print(e)
                pass
            try:
                name = driver.find_element_by_xpath("//h1[@class='mt1kvu ka2E9k uMhVZi FxZV-M RYghuO pVrzNP _9YcI4f _2MyPg2']").text


            except Exception as e:
                print(e)
                pass
            try:
                price = driver.find_element_by_xpath("(//div[@class='_0xLoFW vSgP6A']/span)[1]").text

            except Exception as e:
                print(e)
                pass
            with open('scraped.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([company,name,price])
                f_object.close()
