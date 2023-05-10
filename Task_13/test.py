import numpy as np
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv')
df_18 = pd.read_csv('all_alpha_18.csv')
#diff = df_18['Cyl'].compare(df_08['Cyl'])

# Print the differences
df_08 .rename( columns= {'Sales Area':'Cert Region'}, inplace = True)
df_08.columns = df_08.columns.str.replace(' ', '_').str.lower()
df_18.columns = df_18.columns.str.replace(' ', '_').str.lower()
df_08_v1 = pd.read_csv('data_08_v1.csv')
df_18_v1 = pd.read_csv('data_18_v1.csv')
df = df_08_v1.dropna(inplace= True)
print(df)