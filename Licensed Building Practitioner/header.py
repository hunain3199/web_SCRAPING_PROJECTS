import pandas as pd
df_2 = pd.read_csv("design2.csv", header=None)
df_2.to_csv("design2.csv", header=["Name", "Building practitioner number", "Phone number", "Email address","Website","Location","Company Involvement","Date_Granted","Status_reason","Status_license","License_class ","Area_of_Practice"], index=False)

df_1 = pd.read_csv("design1.csv", header=None)
df_1.to_csv("design1.csv", header=["Name", "Building practitioner number", "Phone number", "Email address","Website","Location","Company Involvement","Date_Granted","Status_reason","Status_license","License_class ","Area_of_Practice"], index=False)

df_3 = pd.read_csv("design3.csv", header=None)
df_3.to_csv("design3.csv", header=["Name", "Building practitioner number", "Phone number", "Email address","Website","Location","Company Involvement","Date_Granted","Status_reason","Status_license","License_class ","Area_of_Practice"], index=False)
