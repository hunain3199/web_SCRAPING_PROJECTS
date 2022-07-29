from _csv import writer

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

def target_html():
    try:
        venue_name = driver.find_element_by_xpath("//h1[@class='MuiTypography-root MuiTypography-h5 MuiTypography-alignCenter']").text
    except:
        venue_name = " "
        pass
    try:
        city_name = driver.find_element_by_xpath(
            "(//p[@class='MuiTypography-root MuiListItemText-secondary MuiTypography-body2 MuiTypography-colorTextSecondary MuiTypography-displayBlock'])[2]").text
    except:
        city_name = " "
        pass
    try:
        country_name = driver.find_element_by_xpath(
            "(//p[@class='MuiTypography-root MuiListItemText-secondary MuiTypography-body2 MuiTypography-colorTextSecondary MuiTypography-displayBlock'])[3]").text
    except:
        country_name = " "
        pass
    try:
        address_name = driver.find_element_by_xpath(
            "(//p[@class='MuiTypography-root MuiListItemText-secondary MuiTypography-body2 MuiTypography-colorTextSecondary MuiTypography-displayBlock'])[1]").text
    except:
        address_name = " "
        pass
    try:
        venue_type = driver.find_element_by_xpath("//h5[@class='MuiTypography-root MuiTypography-subtitle1 MuiTypography-alignLeft']").text
    except:
        venue_type = " "
    try:
        sitting_capacity = driver.find_element_by_xpath("(//h5[@class='MuiTypography-root MuiTypography-subtitle1 MuiTypography-alignCenter'])[1]").text
    except:
        sitting_capacity = " "
    try:
        features = driver.find_element_by_xpath("((//div[@class='MuiGrid-root MuiGrid-container'])[4]/div/span)[1]").text
    except:
        features = " "
    with open('events.csv', 'a', encoding='utf-8', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(
            [venue_name,city_name,country_name,address_name,venue_type,sitting_capacity,features])
        f_object.close()


















# driver = webdriver.Chrome(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get('https://eventup.com/search/?page=70&search=north%20carolina')
driver.implicitly_wait(20)

accept = driver.find_element_by_xpath("//div[@class='termly-styles-buttons__consent-513688']/button")
driver.execute_script("arguments[0].click();", accept)
# webdriver.ActionChains(driver).move_to_element(accept).click(accept).perform()
driver.implicitly_wait(20)

button = driver.find_elements_by_xpath("//div[@class='MuiGridListTile-tile']//button")

for i in button:
    # driver.execute_script("arguments[0].click();", i)
    webdriver.ActionChains(driver).move_to_element(i).click(i).perform()



    # driver.implicitly_wait(20)
# button.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     driver.implicitly_wait(30)
    target_html()
    driver.implicitly_wait(10)


    driver.back()

next_button = driver.find_element_by_xpath("(//span[@class='sr-only'])[4]")
webdriver.ActionChains(driver).move_to_element(next_button).click().perform()

flag = True
while flag:
    try:
        try:
            button = driver.find_elements_by_xpath("//div[@class='MuiGridListTile-tile']//button")


            for i in button:
                # driver.execute_script("arguments[0].click();", i)

                webdriver.ActionChains(driver).move_to_element(i).click(i).perform()

                # driver.implicitly_wait(30)
                # button.click()
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                target_html()
                driver.implicitly_wait(10)




                driver.back()
            next_button = driver.find_element_by_xpath("(//span[@class='sr-only'])[4]")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='sr-only'])[4]")))


            webdriver.ActionChains(driver).move_to_element(next_button).click().perform()
        except:
            driver.refresh()
            button = driver.find_elements_by_xpath("//div[@class='MuiGridListTile-tile']//button")

            for i in button:
                # driver.execute_script("arguments[0].click();", i)

                webdriver.ActionChains(driver).move_to_element(i).click(i).perform()

                # driver.implicitly_wait(30)
                # button.click()
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                target_html()
                driver.implicitly_wait(10)

                driver.back()
            next_button = driver.find_element_by_xpath("(//span[@class='sr-only'])[4]")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='sr-only'])[4]")))

            webdriver.ActionChains(driver).move_to_element(next_button).click().perform()

            continue


    except Exception as e:
        print(e)
        with open('issues.csv', 'a', encoding='utf-8', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([driver.current_url])
            f_object.close()

        flag = False