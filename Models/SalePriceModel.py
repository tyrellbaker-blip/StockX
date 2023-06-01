import re

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

'''
This code loads a dataset from a CSV file using pandas and preprocesses it 
for use in a machine learning algorithm. The main steps in this code include:

Dropping several columns (Order Date, Retail Price, Release Date, Shoe Size, 
and Buyer Region), which are deemed irrelevant or redundant for the purpose 
of the analysis.
Converting the Sale Price column to a float and scaling its values using the 
StandardScaler function from scikit-learn.
Creating a binary target variable ('popular'), which is set to 1 if the sale 
price is greater than 500 and 0 otherwise.
One-hot encoding the categorical variables (Brand and Sneaker Name) using 
pandas' get_dummies() function.
Computing the correlation matrix between the remaining features using 
pandas' corr() function.
Visualizing the correlation matrix using a heatmap generated using seaborn's 
heatmap() function.
In summary, this code performs several data preprocessing steps and 
generates a heatmap to visualize the correlation between different features 
in the dataset, which can be useful for feature selection and engineering 
efforts prior to training a machine learning model.
'''

# Load the data
dataframe = pd.read_csv('../resources/stockx.csv')

# Define the target variable
target = 'num_sales'

# Preprocess the data
dataframe = dataframe.drop(
    ['Order Date', 'Retail Price', 'Release Date', 'Shoe Size',
     'Buyer Region'], axis=1)
dataframe['Sale Price'] = dataframe['Sale Price'].astype(str).apply(
    lambda x: re.sub('[^0-9.]', '', x)).astype(float)
dataframe = pd.get_dummies(dataframe, columns=['Brand', 'Sneaker Name'])
scaler = StandardScaler()
dataframe['Sale Price'] = scaler.fit_transform(dataframe[['Sale Price']])
dataframe['popular'] = (dataframe['Sale Price'] > 500).astype(int)
X = dataframe.drop('popular', axis=1)
y = dataframe['popular']

# Compute the correlation matrix
corr_matrix = X.corr()

# Plot the heatmap
sns.heatmap(corr_matrix, cmap='coolwarm')

# Show the plot
plt.show()
