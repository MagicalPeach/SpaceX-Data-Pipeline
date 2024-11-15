import requests
import pandas as pd

#Pulls data from spacex
response = requests.get('http://api.spacexdata.com/v4/launches')

#Stores data into json format
data = response.json()

#Put into dataframe and extracts top 5 rows
df = pd.DataFrame(data)
print(df.head())

#using pandas only for API fetching
url = 'http://api.spacexdata.com/v4/launches'

#directly moving API fetch into dataframe with Pandas
df = pd.read_json(url)

#extract first 5 rows
print(df.head())

#show column and data type values
print(df.columns)
print(df.dtypes)