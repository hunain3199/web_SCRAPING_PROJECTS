from selenium import webdriver
import time
import csv
from csv import writer


with open('options.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get(i + '?api_key=1fbee64eeded0cb9cdcbd33ad4c21dc6&url=http://httpbin.org/ip')
            sub_links=driver.find_elements_by_xpath("//div[@class = 'findLinks--item']/a")
            for j in sub_links:
                with open('sublinks.csv', 'a', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([j.get_attribute('href')])
                    f_object.close()
