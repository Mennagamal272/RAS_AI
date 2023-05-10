import pandas as pd
import numpy as np

print("Hello! let's explore some US bikeshare data!")
s= input("Would you like to see data for Chicago, New york or Washington ?")
if s == "Chicago":
    df = pd.read_csv('chicago.csv',sep = '\t')
elif s == "New youk":
    df = pd.read_csv('new_york_city.csv',sep = '\t')
elif s == "Washington":
    df = pd.read_csv('washington.csv',sep = '\t')

filter = input("""would you like to filter the data by month, day, both, or not at all ? Type "none" for no time filter.""" )
if filter == "both" :
    month = input("Which month January, February, March, April, May or June ?")
    day   = input("Which day? Please type your response as an integer (e.g.. 1 = sunday )")

print(df.info)