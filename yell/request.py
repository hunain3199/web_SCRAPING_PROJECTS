# import requests
# import csv
#
#
# with open('sublinks.csv', 'r') as file:
#     reader = csv.reader(file)
#     for count, row in enumerate(reader):
#         for i in row:
#             payload = {'api_key': '1fbee64eeded0cb9cdcbd33ad4c21dc6', 'url': i}
#             r = requests.get('http://api.scraperapi.com', params=payload)
#             print(r.status_code)


