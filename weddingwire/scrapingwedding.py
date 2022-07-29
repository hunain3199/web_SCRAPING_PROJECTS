import csv
from _csv import writer
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

import time
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])





driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)


with open('scrapedvenuelinks.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            driver.get(i)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


            try:
                name = driver.find_element_by_xpath("//h1[@class='storefrontHeading__title']").text
            except:
                name = " "
                pass


            try:
                website = driver.find_element_by_xpath("//span[@class='link storefrontHeading__contactItem app-storefront-visit-website']").get_attribute('data-href')
            except:
                website = " "
                pass
            try:
                pricing_pdf_link = driver.find_element_by_xpath("//li[@class='scrollSnap__item app-scroll-snap-item storefrontPricing__slide']/a").get_attribute('href')
            except:
                pricing_pdf_link = " "
                pass
            try:
                facebook_page = driver.find_element_by_xpath("(//div[@class='vendorSocialMedia__linksContainer']/a)[1]").get_attribute('href')
            except:
                facebook_page = " "
                pass
            try:
                Instagram_address = driver.find_element_by_xpath("(//div[@class='vendorSocialMedia__linksContainer']/a)[2]").get_attribute('href')
            except:
                Instagram_address = " "
                pass
            try:
                capacity = driver.find_element_by_xpath("(//div[@class='storefrontDescription__content']/p)[3]").text
            except:
                capacity = " "
                pass
            try:
                address = driver.find_element_by_xpath("//div[@class='app-static-map-header storefrontAddresses__header active']").text
            except:
                address = " "
                pass
            try:
                number = driver.find_element_by_xpath("//span[@class='app-phone-replace']").text
            except:
                number = " "
                pass
            # try:
            #     phone_number = driver.find_element_by_xpath("//button[@class=' storefrontHeading__contactItem storefrontHeading__phone link app-ua-track-event app-default-phone-lead']")
            #     driver.execute_script("arguments[0].scrollIntoView()", phone_number)
            #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class=' storefrontHeading__contactItem storefrontHeading__phone link app-ua-track-event app-default-phone-lead']")))
            #     webdriver.ActionChains(driver).move_to_element(phone_number).click().perform()
            #     time.sleep(2)
            #     number = driver.find_element_by_xpath("//a[@class='leadModalPhoneBox__phoneNumber']").get_attribute('href')
            #     driver.implicitly_wait(10)
            #     exit = driver.find_element_by_xpath("//i[@class='svgIcon svgIcon__close leadFormModal__closeIcon app-modal-close']")
            #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//i[@class='svgIcon svgIcon__close leadFormModal__closeIcon app-modal-close']")))
            #     webdriver.ActionChains(driver).move_to_element(exit).click().perform()
            #     driver.implicitly_wait(10)
            # except:
            #     number = " "
            #     pass
            with open('scrapedwedding.csv', 'a', encoding='utf-8', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(
                    [name, website,address,number ,facebook_page, Instagram_address,capacity,pricing_pdf_link])
                f_object.close()
