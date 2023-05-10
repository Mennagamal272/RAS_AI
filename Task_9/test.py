import pandas as pd

df= pd.read_csv("census_income_data.csv")
print(df.info)

print(f"num of rows is {df.shape[0]}")
print(f"num of columns is {df.shape[1]}")

print("the data type of each column in the dataset is")
print(df.dtypes)

print("index of columns with missing values ")
for i in df.columns[df.isna().any()]:
 print(i)

print("num of unique values of education is ",end="")
print(df["education"].nunique())

print(f"the mean age rounded to the nearest integer is ",end="")
print((int(df["age"].describe()[1].round())))

print(f"the 75th percentile of hours-per-week in this dataset is ",end="")
print((df["hours-per-week"].describe()[6]))
