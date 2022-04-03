import csv
from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

with open('options1.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:

            driver.get(i)
            try:
                name = driver.find_element_by_xpath("//div[@class='formContainer']/h2").text
            except:
                name = " "
                pass

            try:
                building_practitioner_number = driver.find_element_by_xpath("//span[@id= 'ctl00_MainContent_ucLbpDetails_fkLbpNumber_View']").text
            except:
                building_practitioner_number = " "
                pass
            try:
                phone_number = driver.find_element_by_xpath("//span[@id= 'ctl00_MainContent_ucLbpDetails_fkPhoneNumber_View']").text
            except:
                phone_number = " "
                pass
            try:
                email_address = driver.find_element_by_xpath("//span[@id= 'ctl00_MainContent_ucLbpDetails_fkEmailAddress_View']").text
            except:
                email_address = " "
                pass
            try:
                web_address = driver.find_element_by_xpath("//span[@id= 'ctl00_MainContent_ucLbpDetails_fkWebsite_View']").text
            except:
                web_address = " "
                pass
            try:
                location_address = driver.find_element_by_xpath("//span[@id= 'ctl00_MainContent_ucLbpDetails_fkLocation_View']").text
            except:
                location_address = " "
                pass
            try:
                company_involvement = driver.find_element_by_xpath("//span[@id='ctl00_MainContent_ucLbpDetails_ucCompanyInvolvement_rpCompanies_ctl00_tvCompany_View']").text
            except:
                company_involvement = " "
                pass
            try:
                date_granted = driver.find_element_by_xpath("(//table[@class='striped']/tbody/tr/td)[4]").text
            except:
                date_granted = " "
                pass
            try:
                status_reason = driver.find_element_by_xpath("(//table[@class='striped']/tbody/tr/td)[3]").text
            except:
                status_reason = " "
                pass
            try:
                status_license = driver.find_element_by_xpath("(//table[@class='striped']/tbody/tr/td)[2]").text
            except:
                status_license = " "
                pass
            try:
                license_class = driver.find_element_by_xpath("(//table[@class='striped']/tbody/tr/td)[1]/a").text
            except:
                license_class = " "
                pass
            try:
                area_of_practice = driver.find_element_by_xpath("//span[@class='appliedForAops']").text
            except:
                area_of_practice = " "
                pass

            with open('design3.csv', 'a', encoding='utf-8', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([name,building_practitioner_number,phone_number,email_address,web_address,location_address,company_involvement,date_granted,status_reason,status_license,license_class,area_of_practice])
                f_object.close()