from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import re
import pandas as pd
import csv
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from typing import Any
from _csv import writer

def finalScraping() -> None:
    options = webdriver.ChromeOptions()
        # options.add_argument('--incognito')
        # options.add_argument('--disable-site-isolation-trials')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()


    with open('Physicians_links.csv', 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:

                driver.get(i)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    try:
                        req_no:Any = driver.find_element_by_xpath("(//div[@class='jd-item']/span)[1]").text
                    except:
                        req_no = " "
                        pass
                    
                    try:
                        name:Any = driver.find_element_by_xpath("//div[@class='fusion-text fusion-text-4']/h1").text
                    except:
                        name = " "
                        pass

                    try:
                        location_city:Any = driver.find_element_by_xpath("(//div[@class='jd-item']/span)[2]").text
                    except:
                        location_city = " "
                        pass

                    try:
                        location_state:Any = driver.find_element_by_xpath("//div[@class='fusion-text fusion-text-4']/p/span").text
                    except:
                        location_state = " "
                        pass

                    try:
                        department:Any = driver.find_element_by_xpath("//div[@class='jd-item jd-dept2']").text
                        department_text:str = department
                        updated_department:str = re.sub(r'^Department: ', '', department_text)
                        
                    except:
                        updated_department = " "
                        pass

                    try:
                        jd_link:Any = i
                    except:
                        jd_link = " "
                        pass

                    try:
                        job_type:Any = driver.find_element_by_xpath("(//div[@class='jd-item']/span)[4]").text
                    except:
                        job_type = " "
                        pass

                    try:
                        professional_area:Any = driver.find_element_by_xpath("(//div[@class='jd-item']/span)[3]").text
                    except:
                        professional_area = " "
                        pass

                    with open('physicians_cleveland_dataa.csv', 'a', encoding='utf-8', newline='') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(
                            [req_no,name,updated_department,jd_link,location_city,location_state,job_type,professional_area])
                        f_object.close()
                    
                
                except Exception as e:
                    print(e)
                    with open('issues.csv', 'a', encoding='utf-8', newline='') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow([driver.current_url])
                        f_object.close()
            




# df_2 = pd.read_csv("physicians_cleveland_dataa.csv", header=None)
# df_2.to_csv("physicians_cleveland_data.csv", header=["Request No","Name", "Department","Job Description Link","Location (city)","Location (State)","Job Type","Professional Area"])