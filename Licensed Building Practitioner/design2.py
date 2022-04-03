from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://lbp.ewr.govt.nz/publicregister/search.aspx?ap=5&search=1&p=1')
links = driver.find_elements_by_xpath("//table[@class='striped']//tbody/tr/td/a")
for i in links:
    with open('options.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([i.get_attribute('href')])
        f_object.close()

next_btn = driver.find_element_by_xpath("//table[@class='striped']//tfoot/tr/td/a")
next_btn.click()




flag = True
while flag:
    try:
        links = driver.find_elements_by_xpath("//table[@class='striped']//tbody/tr/td/a")
        for i in links:
            with open('options.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([i.get_attribute('href')])
                f_object.close()

        next_btn = driver.find_element_by_xpath("(//table[@class='striped']//tfoot/tr/td/a)[2]")
        next_btn.click()


    except:
        flag = False





