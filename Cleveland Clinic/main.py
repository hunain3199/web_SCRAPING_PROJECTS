from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import pandas as pd
import re
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from typing import Any
from _csv import writer
from final_Scraping import finalScraping
import streamlit as st
st.title("Cleveland Clinic Scraper")
first_page = st.number_input("Enter your First Page Number",value=1)
last_page = st.number_input("Enter your Last Page Number",value=1)
last_pages = last_page + 1


# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# # options.add_argument('--log-level=3')
# options.add_argument('--incognito')
# options.add_argument('--disable-site-isolation-trials')

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver.maximize_window()

# driver.get("https://jobs.clevelandclinic.org/job-search-results/?keyword=Medicine%20Physician&category[]=Physician")


def links_extraction(first,second) -> list[str]:
    list_of_links: list[str] = []
    for i in range(1, 23):
        list_of_links.append(f"https://jobs.clevelandclinic.org/job-search-results/?keyword=Medicine%20Physician&pg={i}&category[]=Physician")

    

    return list_of_links
if st.button("Page Links Function and Physician Links Function"):
    links_list:list[str] = links_extraction(first_page,last_pages)
    def scrapingPhysiciansLinks(links:list[str]) -> list[str]:
        options = webdriver.ChromeOptions()
        # options.add_argument('--incognito')
        # options.add_argument('--disable-site-isolation-trials')

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        physician_links : list[str] = []
        for i in links:
            driver.get(i)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                # cookies = driver.find_element_by_xpath("//a[@id='cn-accept-cookie']")
                # cookies.click()
                job_titles_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='jobTitle']/a")))            
                time.sleep(1)
                for job_link in job_titles_links:
                    with open('Physicians_links.csv', 'a', newline='') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow([job_link.get_attribute("href")])
                        f_object.close()
                        physician_links.append(job_link.get_attribute("href"))
                        
            except:
                continue
        driver.quit()
        return physician_links


    links_of_physcians:list[str]=scrapingPhysiciansLinks(links_list)


    print(links_of_physcians)
    print(len(links_of_physcians))


if st.button("Scraping Function"):
    finalScraping()
    df_2 = pd.read_csv("physicians_cleveland_dataa.csv", header=None)
    df_2.to_csv("physicians_cleveland_data.csv", header=["Request No","Name", "Department","Job Description Link","Location (city)","Location (State)","Job Type","Professional Area"])


if st.button("Clear Output"):
    st.rerun()