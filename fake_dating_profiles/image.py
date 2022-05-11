import csv
import urllib
from _csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://generated.photos/faces/black-race")
driver.maximize_window()

img = driver.find_elements_by_xpath("//div[@class='card-image']/a/img")
for i in img:
    with open('image_link.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([i.get_attribute('src')])
        f_object.close()
    flag = True
    while flag:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='loadmore']"))).click()
            # driver.find_element_by_xpath("//button[@class='loadmore-btn']").click()
            img = driver.find_elements_by_xpath("//div[@class='card-image']/a/img")
            for i in img:
                with open('image_links.csv', 'a', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([i.get_attribute('src')])
                    f_object.close()
        except:
            flag=False










# element =driver.find_element_by_xpath("//button[@class='loadmore-btn']")
# webdriver.ActionChains(driver).move_to_element(element).click(element).perform()












# import wget
#
# # Set up the image URL
# image_url = "https://images.generated.photos/KMyqA5Hp2VH6WjgoDRlZ-_0SYMoUNu8GFcKQQt7rJBI/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDU2NDAzLmpwZw.jpg"
#
# # Use wget download method to download specified image url.
# image_filename = wget.download(image_url)
#
# print('Image Successfully Downloaded: ', image_filename)