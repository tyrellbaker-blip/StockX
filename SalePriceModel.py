import re

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the data
dataframe = pd.read_csv('resources/stockx.csv')

# Define the target variable
target = 'num_sales'

# Preprocess the data
dataframe = dataframe.drop(['Order Date', 'Retail Price', 'Release Date', 'Shoe Size', 'Buyer Region'], axis=1)
dataframe['Sale Price'] = dataframe['Sale Price'].astype(str).apply(lambda x: re.sub('[^0-9.]', '', x)).astype(float)
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
