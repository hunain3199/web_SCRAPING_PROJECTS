from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from csv import writer
link_list =[]
link ='https://www.zalando.co.uk/womens-clothing-dresses'
for i in range(2,103):
    link_list.append(link + '/?p=' + str(i))
print(link_list)

link_list.insert(0, 'https://www.zalando.co.uk/womens-clothing-dresses/')
print(link_list)
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()


for i in link_list:


    driver.get(i)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    product_link =driver.find_elements_by_xpath("//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ']")
    for j in product_link:
        with open('product_links.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([j.get_attribute('href')])
            f_object.close()


# for e in link_list:
#     with open('page_links.csv', 'a', newline='') as f_object:
#         writer_object = writer(f_object)
#         writer_object.writerow([' '.join(str(e))])
#         f_object.close()

# ' '.join(str(e) for e in link_list
#             with open('sublinks.csv', 'a', newline='') as f_object:
#                 writer_object = writer(f_object)
#                 writer_object.writerow([e])
#                 f_object.close()
#          )
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('https://www.zalando.co.uk/womens-clothing-dresses/')
# driver.maximize_window() # For maximizing window
#
#
# #     with open('product_link.csv', 'a', newline='') as f_object:
# #         writer_object = writer(f_object)
# #         writer_object.writerow([i.get_attribute('href')])
# #         f_object.close()
#
# # def scroll_down(driver):
# #     """A method for scrolling the page."""
# #
# #     # Get scroll height.
# #     last_height = driver.execute_script("return document.body.scrollHeight")
# #
# #     while True:
# #
# #         # Scroll down to the bottom.
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #
# #         # Wait to load the page.
# #         time.sleep(2)
# #
# #         # Calculate new scroll height and compare with last scroll height.
# #         new_height = driver.execute_script("return document.body.scrollHeight")
# #
# #         if new_height == last_height:
# #
# #             break
# #
# #         last_height = new_height
# #
# # scroll_down(driver)
#
# product_link =driver.find_elements_by_xpath("//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ']")
# for i in product_link:
#     print(i.get_attribute('href'))
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     wait = WebDriverWait(driver, 10)
#     btn = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@class='DJxzzA PgtkyN']"))
#     ).click()
#     time.sleep(2)
#     product_link = driver.find_elements_by_xpath("//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ']")
#     flag = True
#     while flag:
#         try:
#             for i in product_link:
#                 print(i.get_attribute('href'))
#
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             wait = WebDriverWait(driver, 10)
#             btn = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "//a[@class='DJxzzA PgtkyN']"))
#             ).click()
#             # time.sleep(2)
#             # driver.implicitly_wait(10)
#
#             # accept = driver.find_element_by_xpath("//button[@id='uc-btn-accept-banner']").click()
#
#
#
#
#
#
#         except:
#             flag = False
#
#
#
#
#
#
#
#
#
#
#
#
#



