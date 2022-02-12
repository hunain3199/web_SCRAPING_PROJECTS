from selenium import webdriver
import time
import csv
from csv import writer
from selenium.webdriver.common.by import By


with open('listing.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get(i)
            title = driver.find_element_by_xpath("//h1[@class = 'text-h1 businessCard--businessName']").text

            with open('scraped.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([title])
                f_object.close()































# with open('listing.csv', 'r') as file:
#     reader = csv.reader(file)
#     for count, row in enumerate(reader):
#         for i in row:
#
#             driver = webdriver.Chrome(executable_path='chromedriver.exe')
#             driver.get(i + '?api_key=1fbee64eeded0cb9cdcbd33ad4c21dc6&url=http://httpbin.org/ip')
#
#             # driver.implicitly_wait(10)
#             time.sleep(2)
#             title = driver.findElement(By.xpath("//h1[@class = 'text-h1 businessCard--businessName']")).getText()
#             website = driver.findElement(By.xpath("//a[@class ='btn btn-big btn-yellow businessCard--callToAction']/@href")).getText()
#
#             # category = driver.find_elements("(//span[@itemprop ='name'])[2]")
#             # sub_category = driver.find_elements("(//span[@itemprop ='name'])[3]")
#             listt =[title,website]
#             for j in listt:
#                 with open('scraped.csv', 'a', newline='') as f_object:
#                     writer_object = writer(f_object)
#                     writer_object.writerow([j])
#                     f_object.close()
#
#             # print(title)
#             # print(number)
#             # print(website)
#             # print(category)
#             # print(sub_category)
#                 # with open('scraped.csv', 'a', newline='') as f_object:
#                 #     writer_object = writer(f_object)
#                 #     writer_object.writerow([title,number,website,category,sub_category])
#                 #     f_object.close()
#
#
#
#
#
#
#
#             # # for j in title:
#             #     with open('scraped.csv', 'a', newline='') as f_object:
#             #         writer_object = writer(f_object)
#             #         writer_object.writerow([j.get_attribute('href')])
#             #         f_object.close()