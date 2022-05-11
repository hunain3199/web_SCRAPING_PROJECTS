import pandas as pd
df = pd.read_csv('fake_data.csv')
df['Body Type'] = 'Large'
df.to_csv('fake_data.csv',index=False)

# df_2 = pd.read_csv("fake_data.csv", header=None)
# df_2.to_csv("fake_data.csv", header=["Name", "Height","Age","Birthdate"])