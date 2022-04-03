import time
from csv import writer
from main import links
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='chromedriver.exe')
for i in links:
    driver.get(i)
    # driver.maximize_window()
    try:
        name = driver.find_element_by_xpath("//section[@class='row gutters center-col']/header/h1").text
    except:
        name = " "
        pass
    try:
        regno = driver.find_element_by_xpath("(//article[@class='profile-summary']/p)[1]").text
    except:
        regno = " "
        pass
    try:
        regDate = driver.find_element_by_xpath("(//article[@class='profile-summary']/p)[2]").text
    except:
        regDate = " "
        pass
    try:
        current_status = driver.find_element_by_xpath("(//article[@class='profile-summary']/p)[3]").text
    except:
        current_status = " "
        pass
    try:
        phone = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_pWorkPhone_0']").text
    except:
        phone = " "
        pass
    try:
        email = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_pEmailAddress_0']/a").text
    except:
        email = " "
        pass
    try:
        city = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_pPrivateCity_0']").text
    except:
        city = " "
        pass
    try:
        country = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_pPrivateCountry_0']").text
    except:
        country = " "
        pass
    try:
        company_name = driver.find_element_by_xpath("((//article[@class='profile-summary'])[3]/p)[1]").text
    except:
        company_name = " "
        pass
    try:
        website = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_rptPracticeOds_0_ppWebSite_0']").text
    except:
        website = " "
        pass
    try:
        work_phone = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_rptPracticeOds_0_pPracticePhone_0']").text
    except:
        work_phone = " "
        pass
    try:
        work_city = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_rptPracticeOds_0_pPracticeCity_0']").text
    except:
        work_city = " "
        pass
    try:
        work_country = driver.find_element_by_xpath("//p[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_rptArchiOds_rptPracticeOds_0_pPracticeCountry_0']").text
    except:
        work_country = " "
        pass

    with open('registeredss.csv', 'a',encoding='utf-8', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([name,regno,regDate,current_status,phone,email,city,country,company_name,website,work_phone,work_city,work_country])
        f_object.close()

    time.sleep(1)






