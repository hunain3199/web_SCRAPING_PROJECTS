from faker import Faker
from faker.providers import BaseProvider

import pandas as pd
import csv


faker = Faker()
for i in range(50000):
    name = faker.unique.name_male()
    # address  faker.address()
    # phone = faker.phone_number()
    # email = faker.email()
    # city = faker.city()
    # country = faker.country()
    # state = faker.state()
    # eye_color = faker.color_name()
    # hair_color = faker.color_name()
    height = faker.random_int(153,240)
    age = faker.random_int(18,50)
    birthdate = faker.date_of_birth()

    with open("fake_male_profiles1.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name,height,age,birthdate])
