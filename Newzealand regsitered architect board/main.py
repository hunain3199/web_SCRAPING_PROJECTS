import a as a
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('https://www.nzrab.nz/Search/Architect.aspx?v=2CF7E&r=_&st=_29#result')
#
# url ='https://www.nzrab.nz/Search/Architect.aspx?v=2CF7E&r=_&st=_29'
# df= pd.read_html(url)
# df=df[0]
# df.to_csv('data.csv',index = False)
#
# print(df)
# next_btn_href = driver.find_element_by_xpath("(//span[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_SearchLv_DataPagertop']/a)[2]").get_attribute('href')
# print(next_btn_href)
# next_btn = driver.find_element_by_xpath("(//span[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_SearchLv_DataPagertop']/a)[2]")
# next_btn.click()
# flag = True
# while flag:
#     try:
#         url = 'https://www.nzrab.nz/Search/Architect.aspx?v=2CF7E&r=_&st=_29'
#         df = pd.read_html(url)
#         df = df[0]
#         df.to_csv('data.csv',mode='a', index=False,header=False)
#
#
#         next_btn = driver.find_element_by_xpath("(//span[@id='ContentPlaceHolderBody_ContentPlaceHolderBody_SearchLv_DataPagertop']/a)[2]")
#         next_btn.click()
#     except:
#         flag =False



data = pd.read_csv('registeredarchitectss.csv')
month = data['REG NO'].tolist()
links = []
for i in month:
    links.append('https://www.nzrab.nz/Search/ArchitectDetail.aspx?r='+str(i))

print(len(links))
print(links)

