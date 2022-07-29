import csv
from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            driver.get(i)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            venue_links = driver.find_elements_by_xpath("//a[@class='vendorTile__title  app-vendor-tile-link']")
            for i in venue_links:


                with open('scrapedvenuelinks.csv', 'a', encoding='utf-8', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([i.get_attribute('href')])
                    f_object.close()