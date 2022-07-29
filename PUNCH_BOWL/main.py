import csv
from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def page_link():
    for i in range(1,16):
        with open('links.csv', 'a',encoding='utf-8', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(["https://www.punchbowl.com/vendors/search?category=venues&commit=Search&distance=20&from_index=true&location=RALEIGH%2C+nc&page=" + str(i) + "&search_term=&use_category=true&utf8=✓"])
            f_object.close()


def venue_links():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')


    with open('links.csv', 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:
                driver.get(i)
                time.sleep(2)
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                venue_links = driver.find_elements_by_xpath("//a[@class='vendor-list-entry__name']")
                driver.implicitly_wait(10)
                for i in venue_links:
                    with open('venue_links.csv', 'a', encoding='utf-8', newline='') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow([i.get_attribute('href')])
                        f_object.close()

def venue_details():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()

    with open('venue_links.csv', 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:
                driver.get(i)
                time.sleep(2)

                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    name = driver.find_element_by_xpath("//h1[@class='fn org']").text

                except:
                    name = driver.find_element_by_xpath("//div[@class='vendor_details']/h1").text
                    pass
                try:
                    address = driver.find_element_by_xpath("//p[@class='street-address']").text
                except:
                    address = " "
                    pass
                try:
                    locality = driver.find_element_by_xpath("//span[@class='locality']").text
                except:
                    locality = " "
                    pass
                try:
                    region = driver.find_element_by_xpath("//span[@class='region']").text
                except:
                    region = " "
                    pass
                try:
                    postal_code = driver.find_element_by_xpath("//p[@class='postal-code']").text
                except:
                    postal_code = driver.find_element_by_xpath("//span[@class='postal-code']").text
                    pass
                try:
                    phone_number = driver.find_element_by_xpath("//p[@class='phone_number']").text
                except:
                    try:
                        phone_number = driver.find_element_by_xpath("//li[@class='phone']").text
                    except:
                        phone_number = " "
                        pass
                try:
                    description = driver.find_element_by_xpath("//div[@class='vendor-about-text']/p").text
                except:
                    try:
                        description = driver.find_element_by_xpath("//section[@class='about-text']/div/p").text
                    except:
                        description = " "
                        pass

                with open('punch_bowl.csv', 'a', encoding='utf-8', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([name,phone_number,address,locality,region,postal_code,description])
                    f_object.close()


