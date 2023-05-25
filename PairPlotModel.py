import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
dataframe = pd.read_csv('resources/stockx.csv')

# Preprocess the data
dataframe = dataframe.drop(['Shoe Size', 'Buyer Region'], axis=1)
dataframe['Sale Price'] = dataframe['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)
dataframe['Retail Price'] = dataframe['Retail Price'].str.replace(',', '').str.replace('$', '').astype(float)
dataframe['Release Date'] = pd.to_datetime(dataframe['Release Date'], format='%m/%d/%y').dt.year
dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'], format='%m/%d/%y').dt.year
dataframe['Popular'] = (dataframe['Sale Price'] > 500).astype(int)

# Generate scatter plot matrix
sns.pairplot(dataframe, vars=['Sale Price', 'Retail Price', 'Release Date', 'Order Date'],
             diag_kind='hist', hue='Brand', palette='bright', corner=True)
plt.show()