import numpy as np
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv')
df_18 = pd.read_csv('all_alpha_18.csv')
#df_08 
   #no of samples = 2404
   #no of columns = 18
#print(df_08.shape)
#df_18 
   #no of samples = 1611 
   #no of columns = 18
#print(df_18.shape)   
print(df_08.shape)
df_08 = df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'],axis =1)
print(df_08.shape)
df_08.rename( columns= {'Sales Area':'Cert Region'}, inplace = True)
df_08.columns = df_08.columns.str.replace(' ', '_').str.lower()
df_08.to_csv('data_08_v1.csv', index=False)
df_08_v1 = pd.read_csv('data_08_v1.csv')
df_18_v1 = pd.read_csv('data_18_v1.csv')

df_08_v1 = df_08_v1.query('cert_region == "CA"')
print(df_08_v1.shape)
df_08_v1.drop(['cert_region'],axis =1, inplace = True)
print(df_08_v1.shape)
df_08_v1.dropna(inplace = True)
print(df_08_v1.shape)
df_08_v1.drop_duplicates(inplace = True)
print(df_08_v1.shape)
print(df_08_v1['air_pollution_score'].dtype)
print(df_18_v1['air_pollution_score'].dtype)
df_18_v1['air_pollution_score'] = df_18_v1['air_pollution_score'].astype(float)
df_08_v1['air_pollution_score'] = df_08_v1['air_pollution_score'].str.strip()
df_08_v1['air_pollution_score'] = df_08_v1['air_pollution_score'].str.replace('\D', '').astype(float)
print(df_08_v1['air_pollution_score'].dtype)
print(df_18_v1['air_pollution_score'].dtype)

df_08_hybrid = df_08_v1[df_08_v1['fuel'].str.contains('/')]
df_18_hybrid = df_18_v1[df_18_v1['fuel'].str.contains('/')]

# Make two copies of the hybrid rows
df1_08 = df_08_hybrid.copy()
df2_08 = df_08_hybrid.copy()
df1_18 = df_18_hybrid.copy()
df2_18 = df_18_hybrid.copy()

# Get a list of all columns that are affected
cols_to_split = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg']


# Split the rows by / to two rows for each column
for col in cols_to_split:
    df1_08[col] = df_08_hybrid[col].astype(str).apply(lambda x: x.split('/')[0].strip())
    df2_08[col] = df_08_hybrid[col].astype(str).apply(lambda x: x.split('/')[1].strip() if len(x.split('/')) > 1 else '')
    df1_18[col] = df_18_hybrid[col].astype(str).apply(lambda x: x.split('/')[0].strip())
    df2_18[col] = df_18_hybrid[col].astype(str).apply(lambda x: x.split('/')[1].strip() if len(x.split('/')) > 1 else '')


# Drop the original rows from the dataset
df_08_v1.drop(df_08_hybrid.index, inplace=True)
df_18_v1.drop(df_18_hybrid.index, inplace=True)

# Append the newly created rows to the original dataframe
df_08_v1 = df_08_v1.append(df1_08.append(df2_08)).reset_index(drop=True)
df_18_v1 = df_18_v1.append(df1_18.append(df2_18)).reset_index(drop=True)
for col in ['air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg','greenhouse_gas_score']:
   df_08_v1[col] = df_08_v1[col].astype(float)

# for 2018, convert int to float

print(df_08_v1.dtypes)
