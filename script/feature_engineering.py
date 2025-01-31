import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

# Function to calculate Weight of Evidence (WOE) and Information Value (IV)
def calculate_woe_iv(data, feature, target):
    """
    Calculate Weight of Evidence (WOE) and Information Value (IV) for a given feature.

    Parameters:
    data (pd.DataFrame): Input DataFrame containing the feature and target
    feature (str): Name of the feature column to calculate WOE and IV
    target (str): Name of the target column (binary: 0 or 1)

    Returns:
    pd.DataFrame: DataFrame with calculated WOE and IV values for each category in the feature
    """
    eps = 1e-7  # Small value added to avoid division by zero during calculations
    grouped = data.groupby(feature)[target].agg(['count', 'sum'])  # Group by feature and calculate counts and sums
    grouped['non_event'] = grouped['count'] - grouped['sum']  # Calculate non-events (negative class counts)
    grouped['event_rate'] = grouped['sum'] / grouped['sum'].sum()  # Proportion of positive class (events)
    grouped['non_event_rate'] = grouped['non_event'] / grouped['non_event'].sum()  # Proportion of negative class
    grouped['woe'] = np.log((grouped['event_rate'] + eps) / (grouped['non_event_rate'] + eps))  # Calculate WOE
    grouped['iv'] = (grouped['event_rate'] - grouped['non_event_rate']) * grouped['woe']  # Calculate IV
    return grouped[['woe', 'iv']]  # Return only the WOE and IV columns

# Function for feature engineering on a DataFrame
def feature_engineering(df):
    """
    Perform feature engineering on the given DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing raw data

    Returns:
    pd.DataFrame: DataFrame with newly engineered features
    """

    # Aggregate features based on CustomerId
    print("\n--- Creating Aggregate Features ---")
    df['TotalTransactionAmount'] = df.groupby('CustomerId')['Amount'].transform('sum')  # Total amount per customer
    df['AvgTransactionAmount'] = df.groupby('CustomerId')['Amount'].transform('mean')  # Average amount per customer
    df['TransactionCount'] = df.groupby('CustomerId')['Amount'].transform('count')  # Count of transactions per customer
    df['StdTransactionAmount'] = df.groupby('CustomerId')['Amount'].transform('std')  # Standard deviation of amounts

    # Extract time-based features from the transaction start time
    print("\n--- Extracting Date-Based Features ---")
    df['TransactionHour'] = pd.to_datetime(df['TransactionStartTime']).dt.hour  # Extract hour from timestamp
    df['TransactionDay'] = pd.to_datetime(df['TransactionStartTime']).dt.day  # Extract day from timestamp
    df['TransactionMonth'] = pd.to_datetime(df['TransactionStartTime']).dt.month  # Extract month from timestamp
    df['TransactionYear'] = pd.to_datetime(df['TransactionStartTime']).dt.year  # Extract year from timestamp

    # Encode categorical variables
    print("\n--- Encoding Categorical Variables ---")
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns  # Identify categorical columns
    high_cardinality_cols = [col for col in categorical_cols if df[col].nunique() > 50]  # High cardinality columns
    low_cardinality_cols = [col for col in categorical_cols if df[col].nunique() <= 50]  # Low cardinality columns

    # Apply One-Hot Encoding to low cardinality columns
    if low_cardinality_cols:
        one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')  # Drop the first category to avoid multicollinearity
        one_hot_encoded = pd.DataFrame(one_hot_encoder.fit_transform(df[low_cardinality_cols]),
                                       columns=one_hot_encoder.get_feature_names_out(low_cardinality_cols))
        df = pd.concat([df, one_hot_encoded], axis=1)  # Concatenate the encoded columns with the DataFrame

    # Apply Label Encoding to high cardinality columns
    for col in high_cardinality_cols:
        df[f'{col}_Encoded'] = LabelEncoder().fit_transform(df[col])  # Encode categories into integers

    # Handle missing values in the DataFrame
    print("\n--- Handling Missing Values ---")
    imputer = SimpleImputer(strategy='mean')  # Impute missing values with the mean of each column
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns  # Identify numerical columns
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])  # Apply imputation to numerical columns

    # Normalize/Standardize numerical features
    print("\n--- Normalizing/Standardizing Numerical Features ---")
    scaler = MinMaxScaler()  # Min-Max scaling to normalize data to the range [0, 1]
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])  # Apply scaling to numerical columns

    # Perform feature engineering using Weight of Evidence (WOE)
    print("\n--- Feature Engineering with WOE ---")
    if 'FraudResult' in df.columns:  # Check if the target column 'FraudResult' exists in the DataFrame
        for feature in categorical_cols:
            woe_iv = calculate_woe_iv(df, feature, 'FraudResult')  # Calculate WOE and IV for each categorical feature
            df = df.merge(woe_iv['woe'], how='left', left_on=feature, right_index=True,
                          suffixes=('', f'_WOE_{feature}'))  # Merge WOE values into the DataFrame

    print("Feature Engineering completed successfully!")
    df.head(10)  # Display the first 10 rows of the DataFrame
    return df  # Return the updated DataFrame
