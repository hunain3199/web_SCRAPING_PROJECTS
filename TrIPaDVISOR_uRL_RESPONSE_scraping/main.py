from _csv import writer

import requests
import csv
# response = requests.get('https://www.tripadvisor.com/Hotels-g1000000.html')
# print(response.status_code)
def link_scraping():
    for i in range(1000000,2000001):
        with open('link_scraping1.csv', 'a', encoding='utf-8', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(["https://www.tripadvisor.com/Hotels-g" + str(i) + ".html"])
            f_object.close()

# link_scraping()

def status_code_scraping():
    with open('link_scraping1.csv', 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:
                response = requests.get(i)
                with open('statuscode1.csv', 'a', encoding='utf-8', newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([i,response.status_code])
                    f_object.close()

status_code_scraping()

