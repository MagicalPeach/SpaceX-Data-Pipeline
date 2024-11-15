import requests
import pandas as pd

#Pulls data from spacex
response = requests.get('http://api.spacexdata.com/v4/launches')

#Stores data into json format
data = response.json()

#Put into dataframe and extracts top 5 rows
df = pd.DataFrame(data)
print(df.head())