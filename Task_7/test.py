import pandas as pd
import numpy as np
import statistics as stats
import sys
df = pd.read_csv('chipotle.tsv',sep = '\t')
p=df.mode('index')
d=df[['choice_description']]
#print(p.choice_description)
size=df.shape
#print(df.index)
#print(df.info())
print(df.item_name.mode())
print(df.choice_description.mode())
print(type(df.item_price))
#df.item_price=df.item_price.shape
for i in range(0,df.shape[0]):
   df.item_price.values[i]=float(df.item_price.values[i][1:])

print(df.item_price.values[5])
print(df.item_price)
print(type(df.item_price.values[0]))
#print(df.item_name.mode())
#print(df.item_name.count(df.item_name.mode))
sum=0
for i in range(0,df.shape[0]):
   sum += df.item_price.values[i]
#print(f"average = {sum/df.shape[0]}")   

#print(df.item_name.duplicated().sum())
count = df.item_name.duplicated(keep = 'first')
#print(df.item_name.unique())
list=[df.item_name.unique()]
#print(type(list))
#print(df.item_price)
#print(df.item_price.sum())
#print(df.order_id.max())
count=0
#print(df.order_id.mode('index'))
#print(df.order_id.mode('index').duplicated().sum())
item_counts = df['item_name'].value_counts()
most_ordered_item = item_counts.index[0]
num_ordered = item_counts[0]
print(df.item_name.value_counts().count())
#print(df.quantity.count())
print(f"average = {(df.item_price.values.sum())/df.shape[0]}")

sum=0
for i in range(0,df.shape[0]):
   sum += df.item_price.values[i]
print(f"average = {sum/df.shape[0]}") 
