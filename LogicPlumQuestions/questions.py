import pandas as pd
df=pd.read_csv("uszips.csv")
zipcodes=df['zip']
zip_data=zipcodes.to_json()  #all zip code in json format
print(zip_data)



#fetcing a particualr row
# df.loc[df[‘column name’] condition]

zip_code_row=df.loc[df['zip'] ==601]
zip_code_row_data=zip_code_row.to_json()
print(zip_code_row_data)


#updating population

df.loc[df['zip'] == 601, 'population'] = 10000


zip_code_row=df.loc[df['zip'] ==601]
zip_code_row_data=zip_code_row.to_json()
print(zip_code_row_data)




#adding record


# df.loc[df['column_name'].isin(some_values)]

data=df.loc[df['zip']=="450"]
if data.empty:
    print("empty")