import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

df = pd.read_csv('winequality_edited.csv')

#print(df.query('volatile_acidity < citric_acid'))


# Define low alcohol and high alcohol groups based on alcohol content
low_alcohol = df.query('alcohol <= alcohol.mean()')['quality'].mean()
high_alcohol = df.query('alcohol >= alcohol.mean()')['quality'].mean()

# Calculate the mean quality of each group
print(h_alcohol)
