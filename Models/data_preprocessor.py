import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

'''
Code Description:
This code defines several functions that are used to preprocess and clean a 
dataset. The idea behind this is to prepare the data for use as input in a 
machine learning algorithm, such as training a model, by performing quality 
checks, cleaning, scaling, encoding, and/or reducing its dimensionality.

The load_data() function reads data from one or more CSV files and merges 
them into a single pandas dataframe. It also drops any columns specified to 
be dropped.

The quality_assessment() function performs checks on the data, including 
counting missing values per column, checking for duplicates, printing data 
types, and describing data statistics.

The clean_data() function performs data cleaning on the loaded dataset. This 
includes removing duplicates, filling in any missing values with the mean, 
removing outliers based on z-score, and scaling the numerical data features 
using the Standard Scaler function.

The transform_data() function one-hot encodes any categorical variables 
present in the dataset (i.e. converts them into a numerical form), 
and combines these with the original dataset.

The reduce_data() function uses Principal Component Analysis (PCA) to 
perform dimensionality reduction on the dataset, as specified by n_components.

Finally, preprocess_data() combines all of these functions together, 
depending on what data cleaning steps we need to do, and either returns the 
original or transformed dataset, or both.

Overall, this code sets up a framework for automating and standardizing the 
preprocessing of a dataset, so that it can be easily used as input to a 
machine learning algorithm.

'''


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
    if len(df) > 1:
        df = pd.concat(dfs, axis=0, ignore_index=True)
    else:
        df = dfs[0]

    return df

#TODO: Fix the load data function

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

# message
