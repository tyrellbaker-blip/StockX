# TODO: We're going to implement a different algorithm, decision trees:
# TODO: IMPORTS(BELOW)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# a. Read & load original data into a DataFrame
df = pd.read_csv('../resources/stockx.csv')

# b. Identify incompatible columns and drop them from the DataFrame
incompatible_cols = ['Order Date']
df.drop(incompatible_cols, axis=1, inplace=True)


# c. Cleaning the DataFrame by one-hot encoding categorical features

def clean_data(df):
    # Remove dollar signs and commas from price columns
    df['Sale Price'] = df['Sale Price'].str.replace(',', '').str.replace('$', '').astype(float)
    df['Retail Price'] = df['Retail Price'].str.replace(',', '').str.replace('$', '').astype(float)

    # Check for and remove any remaining non-numeric values in 'Retail Price' column
    non_numeric = df['Retail Price'].apply(lambda x: isinstance(x, str))
    df.loc[non_numeric, 'Retail Price'] = np.nan

    # One-hot encode the categorical columns (excluding 'Brand')
    cat_cols = [col for col in df.columns if df[col].dtype == 'object' and col != 'Brand']
    encoded_df = pd.get_dummies(df[cat_cols])

    # Concatenate the one-hot encoded data with the 'Retail Price' column
    cleaned_df = pd.concat([df['Retail Price'], encoded_df], axis=1)

    # Add back the 'Brand' column
    cleaned_df['Brand'] = df['Brand']

    return cleaned_df


cleaned_df = clean_data(df)

# d. Split the data into training and testing sets
X = cleaned_df.drop(['Brand'], axis=1)
y = cleaned_df['Brand']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# e. Create the decision tree model
tree_model = DecisionTreeClassifier()

# f. Fit the model to the training data
tree_model.fit(X_train, y_train)

# g. Visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(tree_model, feature_names=X.columns, class_names=tree_model.classes_,
          filled=True)
plt.show()

# h. Use the model to make predictions on the testing data
y_pred = tree_model.predict(X_test)

# i. Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

#
#