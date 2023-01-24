from _csv import writer
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time



options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()


driver.get("https://www.indeed.com/viewjob?jk=8bb00d65900b43be&from=serp&vjs=3")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

try:
    job_title = driver.find_element_by_xpath(
        "//h1[@class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']").text
except:
    job_title = " "
    pass

try:
    company_name = driver.find_element_by_xpath(
        "//div[@class='css-czdse3 eu4oa1w0']/a").text
except:
    company_name = " "
    pass
try:
    company_reviews = driver.find_element_by_xpath(
        "//span[@class='css-xvmbeo e1wnkr790']/a").text
except:
    company_reviews = " "
    pass
try:
    salary_range = driver.find_element_by_xpath(
        "(//span[@class='css-2iqe2o eu4oa1w0'])[1]").text
except:
    salary_range = " "
    pass
try:

    full_time = driver.find_element_by_xpath(
        "(//div[@class='icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle']/div)[2]/div").text
    full_times = driver.find_element_by_xpath(
        "//span[@class='jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs']").text

    job_time=[]
    if (full_time == 'Full-time' or full_time == 'Remote' or full_times == 'Full-time' or full_times == 'Remote'):
        job_time.append(full_time)
        job_time.append(full_times)



except:
    job_time = " "
    pass

try:
    benefits = []
    benefit = driver.find_element_by_xpath(
        "(//h2[@class='jobsearch-JobDescriptionSection-jobDescriptionTitle'])[1]/div").text

    if (benefit == 'Pulled from the full job description'):

        benefit1 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[1]").text
        benefits.append(benefit1)


        benefit2 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[2]").text
        benefits.append(benefit2)

        benefit3 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[3]").text
        benefits.append(benefit3)
        benefit4 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[4]").text
        benefits.append(benefit4)

        benefit5 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[5]").text
        benefits.append(benefit5)

        benefit6 = driver.find_element_by_xpath(
            "(//div[@class='css-4l8g94 eu4oa1w0']/div/div/div/div)[6]").text
        benefits.append(benefit6)




except:
    pass

try:
    fulldescript = []
    fulldescription = driver.find_element_by_xpath(
        "//h2[@id='jobDescriptionTitle']").text
    print(fulldescription)

    if (fulldescription == 'Full Job Description'):
        full_description1 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[1]").text
        fulldescript.append(full_description1)

        full_description2 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[2]").text
        fulldescript.append(full_description2)

        full_description3 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[3]").text
        fulldescript.append(full_description3)

        full_description4 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[4]").text
        fulldescript.append(full_description4)

        full_description5 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[5]").text
        fulldescript.append(full_description5)

        full_description6 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[6]").text
        fulldescript.append(full_description6)

        full_description7 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[7]").text
        fulldescript.append(full_description7)

        full_description8 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[8]").text
        fulldescript.append(full_description8)

        full_description9 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[9]").text
        fulldescript.append(full_description9)

        full_description10 = driver.find_element_by_xpath("(//div[@id='jobDescriptionText']/div/*)[10]").text
        fulldescript.append(full_description10)
        print(fulldescript)

except:
    pass

try:
    job_activity = driver.find_element_by_xpath("(//ul[@class='css-659xjq eu4oa1w0']/li/span)[2]").text

except:
    job_activity = " "
    pass

 try:
    apply_link = driver.find_element_by_xpath("//div[@class='icl-u-xs-hide icl-u-lg-block icl-u-lg-textCenter']/a").get_attribute('href')
except:
    apply_link = " "
    pass


with open('indeed.csv', 'a', encoding='utf-8', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow([job_title, company_name, company_reviews, job_time, salary_range, benefits, fulldescript, job_activity,apply_link])
