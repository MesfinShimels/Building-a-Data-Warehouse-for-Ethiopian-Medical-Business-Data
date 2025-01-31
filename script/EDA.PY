import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform Exploratory Data Analysis (EDA) on a DataFrame
def perform_eda(df):
    """
    Perform Exploratory Data Analysis (EDA) on the given DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing data to be analyzed

    Returns:
    None: Displays plots and prints summaries of the data
    """

    # Overview of the dataset
    print("\n--- Dataset Overview ---")
    print(f"Number of rows: {df.shape[0]}")  # Print the number of rows in the DataFrame
    print(f"Number of columns: {df.shape[1]}")  # Print the number of columns in the DataFrame
    print("\n--- Data Types ---")
    print(df.dtypes)  # Print the data types of each column in the DataFrame

    # Summary statistics for the dataset
    print("\n--- Summary Statistics ---")
    print(df.describe(include='all'))  # Print summary statistics, including for numerical and categorical data

    # Check for missing values in the dataset
    print("\n--- Missing Values ---")
    missing_values = df.isnull().sum()  # Calculate the number of missing values per column
    print(missing_values[missing_values > 0])  # Print columns with missing values and their counts

    # Plot histograms for numerical features
    print("\n--- Distribution of Numerical Features ---")
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns  # Identify numerical columns
    df[numerical_features].hist(bins=30, figsize=(15, 10))  # Plot histograms for each numerical column
    plt.suptitle('Histograms of Numerical Features')  # Add a title to the histograms
    plt.show()

    # Plot count plots for categorical features
    print("\n--- Distribution of Categorical Features ---")
    categorical_features = df.select_dtypes(include=['object', 'category']).columns  # Identify categorical columns
    for feature in categorical_features:
        plt.figure(figsize=(8, 4))  # Set figure size for the plot
        sns.countplot(data=df, x=feature, order=df[feature].value_counts().index)  # Plot count plot for the feature
        plt.title(f'Distribution of {feature}')  # Add a title to the plot
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.show()

    # Correlation analysis for numerical features
    print("\n--- Correlation Analysis ---")
    if len(numerical_features) > 1:  # Ensure there are at least two numerical features for correlation analysis
        corr_matrix = df[numerical_features].corr()  # Compute the correlation matrix
        plt.figure(figsize=(10, 8))  # Set figure size for the heatmap
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)  # Plot the heatmap with annotations
        plt.title('Correlation Matrix')  # Add a title to the heatmap
        plt.show()
    else:
        print("Not enough numerical features for correlation analysis.")  # Handle case with insufficient numerical features

    # Outlier detection using box plots for numerical features
    print("\n--- Outlier Detection ---")
    for feature in numerical_features:
        plt.figure(figsize=(8, 4))  # Set figure size for the box plot
        sns.boxplot(data=df, x=feature)  # Plot a box plot for the feature
        plt.title(f'Boxplot of {feature}')  # Add a title to the box plot
        plt.show()

    print("EDA completed successfully!")  # Print a success message when EDA is complete
