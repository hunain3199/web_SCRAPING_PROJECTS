from selenium import webdriver
import time
import pandas as pd
import csv

def pagesData(filename,summary_file,further_file,contact_file,date_file,constraint_file,document_file):

    # Header Adding in Summary File
    fieldsummary=['Reference','Alternative Reference','Application Received','Application Validated','Address','Proposal','Status','Decision','Decision Issued Date','Appeal Status','Appeal Decision']
    with open(summary_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fieldsummary)
    fieldfurther = ['Application Type', 'Expected Decision Level', 'Case Officer', 'Parish', 'Ward',
                    'District Reference', 'Applicant Name', 'Agent Name', 'Agent Company Name', 'Agent Address',
                    'Environmental Assessment Requested']
    with open(further_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fieldfurther)

    with open(contact_file, 'a') as f:
        writer = csv.writer(f)

    fielddates = ['Application Received Date', 'Application Validated Date', 'Expiry Date', 'Actual Committee Date', 'Latest Neighbour Consultation Date',
                    'Neighbour Consultation Expiry Date', 'Standard Consultation Date', 'Standard Consultation Expiry Date', 'Last Advertised In Press Date', 'Latest Advertisement Expiry Date	',
                    'Last Site Notice Posted Date','Latest Site Notice Expiry Date	','Internal Target Date	','Agreed Expiry Date','Decision Made Date','Decision Issued Date',
                  'Permission Expiry Date','Decision Printed Date','Environmental Impact Assessment Received','Determination Deadline','Temporary Permission Expiry Date']
    with open(date_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fielddates)

    fieldconstraints = ['Name', 'Constraint Type', 'Status']
    with open(constraint_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fieldconstraints)

    fielddocument = ['Date Published', 'Document Type', 'Measure', 'Drawing Number', 'Description','View']
    with open(document_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fielddocument)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:
                driver = webdriver.Chrome(executable_path='chromedriver.exe')
                driver.get(i)

                time.sleep(2)
                try:
                    summary = driver.find_element_by_xpath("//a[@id = 'subtab_summary']").get_attribute("href")
                    df = pd.read_html(summary)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv(summary_file,mode='a',header = False, index=False)
                except Exception as e:
                    print(e)
                    pass
                try:
                    further = driver.find_element_by_xpath("//a[@id = 'subtab_details']").get_attribute("href")
                    df = pd.read_html(further)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv(further_file, mode='a', header=False, index=False)
                except Exception as e:
                    print(e)
                    pass
                try:
                    contacts = driver.find_element_by_xpath("//a[@id = 'subtab_contacts']").get_attribute("href")
                    df = pd.read_html(contacts)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv(contact_file, mode='a', header=False, index=False)
                except Exception as e:
                    pass
                try:
                    dates = driver.find_element_by_xpath("//a[@id = 'subtab_dates']").get_attribute("href")
                    df = pd.read_html(dates)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv(date_file, mode='a', header=False, index=False)
                except Exception as e:
                    pass

                try:
                    constraints = driver.find_element_by_xpath("//a[@id = 'tab_constraints']").get_attribute("href")
                    df = pd.read_html(constraints)
                    df[0].to_csv(constraint_file, mode='a', header = False, index=False)
                except Exception as e:
                    pass
                try:
                    documents = driver.find_element_by_xpath("//a[@id = 'tab_documents']").get_attribute("href")
                    df = pd.read_html(documents)
                    df[0].to_csv(document_file, mode='a', header = False, index=False)

                except Exception as e:
                    pass


                driver.close()