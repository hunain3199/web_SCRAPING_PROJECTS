import pandas as pd

df = pd.read_csv("registeredss.csv", header=None)
df.to_csv("registeredss.csv", header=["NAME", "REG NO", "REG DATE", "CURRENT STATUS","PHONE","EMAIL","CITY","COUNTRY","COMPANY NAME","WEBSITE","WORK PHONE","WORK CITY","WORK COUNTRY"], index=False)
