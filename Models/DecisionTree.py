# TODO: We're going to implement a different algorithm, decision trees:
# TODO: IMPORTS(BELOW)
import pandas as pd
import sklearn.tree
import sklearn.model_selection
import sklearn.metrics
from data_preprocessor import clean_data

'''
pandas for data manipulation.
sklearn.tree for creating decision tree models.
sklearn.model_selection for splitting the data into training and testing
sets.
sklearn.metrics for evaluating the performance of the model.
'''

# TODO: Load the data from the CSV file into a pandas dataframe using the
#  read_csv() function. Preprocess the data by: Removing unnecessary columns
#  from the dataset.v Cleaning the data (i.e., imputing missing values,
#  removing outliers, and scaling the features). Transforming categorical
#  variables into one-hot encoded numerical variables (if necessary). This
#  can be done manually or by calling a pre-written function such as the
#  preprocess_data() function from data_processor.py Look in that module for
#  an explanation of how to use it.
#

# a. Read & Loaded original data into a dataframe
df = pd.read_csv('../resources/stockx.csv')
#print(df.head(5))
#column_headers_original = list(df.columns.values)
#print("The Original Column Header :", column_headers_original)

# b. Dropping unnecessary columns
df_1 = df.drop(['Order Date', 'Retail Price', 'Release Date', 'Shoe Size', 'Buyer Region'], axis=1)
column_headers = list(df_1.columns.values)
print("The Column Header after dropping columns :", column_headers)
print(df_1.head(10))

# c. Cleaning the dataframe
cleanedDataframe = clean_data(df_1)

#
# TODO: Define the target variable for classification. In this case,
#  the target variable is "popular".
#
# TODO: Split the data into input and target variables using the drop() method.

# TODO: Split the data into training and testing sets using the
#  train_test_split() function.
#
# TODO: 1. Create a DecisionTreeClassifier object.
# TODO: 2. Fit the classifier to the training data using the fit() method.
# TODO: 3. Make predictions on the test data  using the predict() method.
# TODO: 4. Evaluate the performance of the model using the accuracy_score()
#  function.
# TODO: 5. Print the accuracy of the model.
