import pandas as pd
import csv
# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'Book1.xlsx'

# Read the Excel file
data = pd.read_excel(file_path)

# Access the first column and save its values into a list
first_column_values = data.iloc[:, 0].tolist()

# Print the list of values from the first column
print(first_column_values)

from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import pandas as pd
import re
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from typing import Any
from _csv import writer
import streamlit as st

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()
for i in first_column_values:
    driver.get(i)
    time.sleep(1)
    annual = driver.find_element_by_xpath("(//button[@class='VfPpkd-AznF2e WbUJNb FEsNhd KlyVq'])[1]")
    driver.execute_script("arguments[0].click();", annual)
    balancesheet = driver.find_element_by_xpath("(//div[@class='oX8Xbb Tj1T2'])[2]")
    driver.execute_script("arguments[0].click();", balancesheet)
    cashflow = driver.find_element_by_xpath("(//div[@class='oX8Xbb Tj1T2'])[3]")
    driver.execute_script("arguments[0].click();", cashflow)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    

    try:
        name = driver.find_element_by_xpath("//div[@class='zzDege']").text
    except:
        name = " "


    company_data = {
    "Company Name": name,
    "Current Stock Price": " ",
    "Market Cap": " ",
    "Dividend Yield": " ",
    "P/E Ratio": " ",
    "52-week high/low (Year Range)":" ",
    "Earnings Per Share": " ",
    "Avg Volume":" ",
    "Previous Close":" ",
    "Day Range":" ",
    "Primary Exchange":" ",
    "Revenue":" ",
    "Operating Expense":" ",
    "Net Income":" ",
    "Net Profit Margin":" ",
    "EBITDA":" ",
    "Effective tax rate":" ",
    "Balance Sheet":" ",
    "Cash and short-term investments":" ",
    "Total Assets":" ",
    "Total Liabilities":" ",
    "Total Equity":" ",
    "Shares Outstanding":" ",
    "Price to book":" ",
    "Return on Assets":" ",
    "Return on capital":" ",
    "Cashflow":" ",
    "CashFlow Net Income":" ",
    "Cash from operations":" ",
    "Cash from investing":" ",
    "Cash from financing":" ",
    "Net change in cash":" ",
    "Free cash flow":" "









}
    
    try:
        company_data["Current Stock Price"] = driver.find_element_by_xpath("//div[@class='AHmHk']/span/div/div").text
        company_data["Market Cap"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[4]/div").text
        company_data["Dividend Yield"]  = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[7]/div").text
        company_data["P/E Ratio"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[6]/div").text
        company_data["52-week high/low (Year Range)"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[3]/div").text
        company_data["Earnings Per Share"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[6]/td)[2]").text
        company_data["Avg Volume"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[5]/div").text
        company_data["Previous Close"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[1]/div").text
        company_data["Day Range"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[2]/div").text
        company_data["Primary Exchange"] = driver.find_element_by_xpath("(//div[@class='gyFHrc'])[8]/div").text
        company_data["Revenue"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[2]/td)[2]").text
        company_data["Operating Expense"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[3]/td)[2]").text
        company_data["Net Income"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[4]/td)[2]").text
        company_data["Net Profit Margin"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[5]/td)[2]").text
        company_data["EBITDA"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[7]/td)[2]").text
        company_data["Effective tax rate"] = driver.find_element_by_xpath("((//table[@class='slpEwd']/tr)[8]/td)[2]").text
        company_data["Balance Sheet"] = " "
        company_data["Cash and short-term investments"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[2]/td)[2]").text
        company_data["Total Assets"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[3]/td)[2]").text
        company_data["Total Liabilities"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[4]/td)[2]").text
        company_data["Total Equity"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[5]/td)[2]").text
        company_data["Shares Outstanding"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[6]/td)[2]").text
        company_data["Price to book"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[7]/td)[2]").text
        company_data["Return on Assets"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[8]/td)[2]").text
        company_data["Return on capital"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[2]/tr)[9]/td)[2]").text
        company_data["Cashflow"] = " "
        company_data["CashFlow Net Income"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[2]/td)[2]").text
        company_data["Cash from operations"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[3]/td)[2]").text
        company_data["Cash from investing"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[4]/td)[2]").text
        company_data["Cash from financing"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[5]/td)[2]").text
        company_data["Net change in cash"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[6]/td)[2]").text
        company_data["Free cash flow"] = driver.find_element_by_xpath("(((//table[@class='slpEwd'])[3]/tr)[7]/td)[2]").text


    
    
    
    except:
        
        pass
    

    df = pd.DataFrame([company_data])

    # Save the data to a CSV file with the company name as the filename
    csv_file_name = f"{name}.csv"
    df.to_csv(csv_file_name, index=False)

    # Save the data to an Excel file with the company name as the filename
    excel_file_name = f"{name}.xlsx"
    df.to_excel(excel_file_name, index=False)



    

# Read the CSV file
    time.sleep(5)
    df_csv = pd.read_csv(csv_file_name)

    # Extract the first two rows
    first_two_rows = df_csv.head(2)

    # Transpose the data to convert rows to columns
    transposed_data = first_two_rows.T

    # Write the transposed data to a new CSV file
    transposed_csv_file_name = f"{name}.csv"
    transposed_data.to_csv(transposed_csv_file_name, header=False)

    # Convert the transposed data to XLSX format
    transposed_xlsx_file_name = f"{name}.xlsx"
    transposed_data.to_excel(transposed_xlsx_file_name, header=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # with open(f"{name}.csv", 'r') as file:
    #     csv_reader = csv.reader(file)
    #     rows = list(csv_reader)

    # # Extract the first two rows
    # first_two_rows = rows[:2]

    # # Transpose the data to convert rows to columns
    # columns = list(zip(*first_two_rows))

    # # Write the transposed data to a new CSV file
    # with open(f"{name}.csv", 'w', newline='') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerows(columns)


    