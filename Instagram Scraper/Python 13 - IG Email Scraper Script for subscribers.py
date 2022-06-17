import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import csv

UserData = []

driver = webdriver.Chrome(executable_path='')
driver.get("https://www.instagram.com")

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")

log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()

with open('','r') as csv_file:
	csv_reading = csv.reader(csv_file)

	for line in csv_reading:
		links = line[1]
		try:
			page = driver.get(links + "?__a=1")
		except Exception as e:
			page = None
		try:
			soup = BeautifulSoup(driver.page_source, "html.parser").get_text()
		except Exception as e:
			soup = None
		try:
			jsondata = json.loads(soup)
		except Exception as e:
			jsondata = None

		try:
			biography = jsondata["graphql"]["user"]["biography"]
		except Exception as e:
			biography = None

		try:
			externalurl = jsondata["graphql"]["user"]["external_url"]
		except Exception as e:
			externalurl = None
		try:
			followers = jsondata["graphql"]["user"]["edge_followed_by"]["count"]
		except Exception as e:
			followers = None
		try:
			following = jsondata["graphql"]["user"]["edge_follow"]["count"]
		except Exception as e:
			following = None
		try:
			businessacount = jsondata["graphql"]["user"]["is_business_account"]
		except Exception as e:
			businessacount = None
		try:
			emails = jsondata["graphql"]["user"]["business_email"]
		except Exception as e:
			emails = None

		element_info = {
			'Biography': biography,
			'ExternalURL': externalurl,
			'Follower': followers,
			'Following': following,
			'BusinessIG': businessacount,
			'Email': emails
		}

		UserData.append(element_info)
		df = pd.DataFrame(UserData)
		print(df)
		df.to_csv('')
