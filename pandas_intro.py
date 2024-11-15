import pandas as pd
data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy'
    ],
    'launches':[5,100,3]
}

df = pd.DataFrame(data)

print(df)

#Selecting specific column - selecting rocket column
print(df['rocket'])

#Filtering Rows into new data frame - selecting row where rocket value is Falcon 9
falcon9_df = df[df['rocket'] == 'Falcon 9']
print(falcon9_df)

#Filtering Rows where rockets had more than 5 launches
greater_than_5_launches_df = df[df['launches'] > 5]
print(greater_than_5_launches_df)


#Adding new columns into original dataframe
df['success_rate'] = [0.4, 0.98, 1.0]
print(df)