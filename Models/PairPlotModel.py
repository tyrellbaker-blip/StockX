import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
This code uses matplotlib and seaborn libraries to create a scatterplot 
matrix from a dataset. The scatterplot matrix visualizes the pairwise 
relationships between different variables in the dataset, allowing us to 
explore correlations and patterns in the data.

The dataset used is loaded from a CSV file using pandas. Several 
preprocessing steps are performed on the data, including dropping columns 
that are not needed, converting string values to float or datetime, 
and creating a new column based on the Sale Price column.

The pairplot() function from Seaborn is then used to generate the 
scatterplot matrix. The vars parameter specifies the columns to be included 
in the matrix, diag_kind specifies the type of plot to use on the diagonal (
in this case, histograms), hue specifies the color variable (in this case, 
Brand), palette specifies the color palette to use, and corner specifies 
whether to show the lower triangle or upper triangle of the matrix.

Finally, plt.show() is called to display the scatterplot matrix.

Overall, this code provides a quick and easy way to visualize the 
relationships between different variables in a dataset, and can help 
identify any patterns or correlations that may exist.

'''


# Load the data
dataframe = pd.read_csv('../resources/stockx.csv')

# Preprocess the data
dataframe = dataframe.drop(['Shoe Size', 'Buyer Region'], axis=1)
dataframe['Sale Price'] = dataframe['Sale Price'].str.replace(',',
                                                              '').str.replace(
    '$', '').astype(float)
dataframe['Retail Price'] = dataframe['Retail Price'].str.replace(',',
                                                                  '').str.replace(
    '$', '').astype(float)
dataframe['Release Date'] = pd.to_datetime(dataframe['Release Date'],
                                           format='%m/%d/%y').dt.year
dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'],
                                         format='%m/%d/%y').dt.year
dataframe['Popular'] = (dataframe['Sale Price'] > 500).astype(int)

# Generate scatter plot matrix
sns.pairplot(dataframe,
             vars=['Sale Price', 'Retail Price', 'Release Date', 'Order Date'],
             diag_kind='hist', hue='Brand', palette='bright', corner=True)
plt.show()
