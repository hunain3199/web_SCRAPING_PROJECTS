import csv
from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:

            driver.get(i)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                name = driver.find_element_by_xpath("//div[@class='vendor-name-container--558cf']/h1").text
            except:
                name = " "
                pass

            try:
                address = driver.find_element_by_xpath(
                    "(//div[@class='contact-info--50b10 body1--c3a01']/span)[1]").text
            except:
                address = " "
                pass
            try:
                website = driver.find_element_by_xpath(
                    "(//span[@class='link--ed1c2']/a)[5]").get_attribute('href')
            except:
                website = " "
                pass
            try:
                phone_number = driver.find_element_by_xpath(
                    "(//div[@class='contact-info--50b10 body1--c3a01']/span)[2]").text
            except:
                phone_number = " "
                pass
            try:
                facebook_page = driver.find_element_by_xpath(
                    "(//span[@class='link--ed1c2'])[1]/a").get_attribute('href')
            except:
                facebook_page = " "
                pass
            try:
                twitter_address = driver.find_element_by_xpath(
                    "(//span[@class='link--ed1c2'])[2]/a").get_attribute('href')
            except:
                twitter_address = " "
                pass
            try:
                price_pdf_link = driver.find_element_by_xpath(
                    "//a[@class='btn--5d134 primary-link--4e35b']").get_attribute('href')
            except:
                price_pdf_link = " "
                pass
            with open('scrapedKnot.csv', 'a', encoding='utf-8', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(
                    [name,address,website,phone_number,facebook_page,twitter_address,price_pdf_link])
                f_object.close()