import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

"""
The preprocess_data() function in data_processor.py is designed to 
preprocess data before modeling. It takes the following arguments:

file_path: Path to the CSV file containing the data.
drop_cols: List of columns to drop from the dataset.
quality_assessment_flag: Boolean value indicating whether to perform quality 
assessment on the data (default is True).
clean_data_flag: Boolean value indicating whether to clean the data (default 
is True).
transform_data_flag: Boolean value indicating whether to transform the data 
(default is True).
reduce_data_flag: Boolean value indicating whether to reduce the dimensions 
of the data using PCA (default is False).
n_components: Number of components to retain after reducing the dimensions 
of the data (default is 2).
Here's what each of the functions within preprocess_data() do:

load_data(): Loads the data from one or more CSV files into a pandas 
dataframe. If multiple CSV files are specified, the function concatenates 
them into a single dataframe.

quality_assessment(): Performs quality assessment on the data and prints the 
following information:

Number of missing values per column
Number of duplicates
Data types of the columns
Basic statistics for the numerical columns
This information can be used to identify and fix quality issues in the data.

clean_data(): Cleans the data by:

Dropping any duplicate rows.
Imputing missing values with the mean of their respective columns.
Removing outliers using the z-score method.
Scaling the numerical features to have zero mean and unit variance.
This helps to improve the quality of the data and makes it suitable for 
processing by machine learning algorithms.

transform_data(): Transforms the categorical variables in the data into 
one-hot encoded numerical variables. This is necessary because many machine 
learning algorithms cannot process categorical data directly.

reduce_data(): Reduces the dimensions of the data using principal component 
analysis (PCA). This can be useful for visualizing high-dimensional data or 
reducing the computational load of machine learning algorithms.

Overall, the preprocess_data() function provides a flexible and 
comprehensive way to preprocess data before modeling.
"""

def load_data(file_paths, drop_cols=None):
    dfs = []

    # Load data from each file path into a separate dataframe
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        if drop_cols is not None:
            df = df.drop(columns=drop_cols)
        dfs.append(df)

    # Merge dataframes into a single dataframe if multiple file paths are
    # provided
    if len(dfs) > 1:
        df = pd.concat(dfs, axis=0, ignore_index=True)
    else:
        df = dfs[0]

    return df


def quality_assessment(df):
    # Check for missing values
    num_missing = df.isnull().sum()
    print(f"Number of missing values per column:\n{num_missing}")

    # Check for duplicates
    num_duplicates = df.duplicated().sum()
    print(f"Number of duplicates: {num_duplicates}")

    # Check data types
    print(f"Data types:\n{df.dtypes}")

    # Check data statistics
    print(f"Data statistics:\n{df.describe()}")

    return df


def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values with mean
    imputer = SimpleImputer(strategy='mean')
    df[df.select_dtypes(
        include=['int', 'float']).columns] = imputer.fit_transform(
        df.select_dtypes(include=['int', 'float']))

    # Remove outliers using z-score
    z_scores = (df.select_dtypes(include=['int', 'float']) - df.select_dtypes(
        include=['int', 'float']).mean()) / df.select_dtypes(
        include=['int', 'float']).std()
    df = df[(z_scores.abs() < 3).all(axis=1)]

    # Feature scaling
    scaler = StandardScaler()
    df[df.select_dtypes(
        include=['int', 'float']).columns] = scaler.fit_transform(
        df.select_dtypes(include=['int', 'float']))

    return df


def transform_data(df):
    # One-hot encode categorical variables
    encoder = OneHotEncoder()
    df_encoded = pd.DataFrame(
        encoder.fit_transform(df.select_dtypes(include=['object'])).toarray(),
        columns=encoder.get_feature_names(
            df.select_dtypes(include=['object']).columns.tolist()))
    df.drop(columns=df.select_dtypes(include=['object']), inplace=True)
    df = pd.concat([df_encoded, df], axis=1)

    return df


def reduce_data(df, n_components=2):
    # PCA for dimensionality reduction
    pca = PCA(n_components=n_components)
    df_reduced = pd.DataFrame(pca.fit_transform(df))

    return df_reduced


def preprocess_data(file_path, drop_cols=None, quality_assessment_flag=True,
                    clean_data_flag=True, transform_data_flag=True,
                    reduce_data_flag=False, n_components=2):
    # Load data from file into a pandas dataframe
    df = load_data(file_path, drop_cols)

    # Perform quality assessment, if enabled
    if quality_assessment_flag:
        df = quality_assessment(df)

    # Perform data cleaning, if enabled
    if clean_data_flag:
        df = clean_data(df)

    # Perform data transformation, if enabled
    if transform_data_flag:
        df = transform_data(df)

    # Perform data reduction, if enabled
    if reduce_data_flag:
        df = reduce_data(df, n_components=n_components)

    return df
