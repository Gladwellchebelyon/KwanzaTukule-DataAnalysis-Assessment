import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# List all files in the current directory
print("Files in current directory:")
for file in os.listdir():
    print(file)

# Try to open the file
file_path = "Case Study Data - Read Only - case_study_data_2025-01-16T06_49_12.19881Z.csv"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"\nFile contents:\n{content}")
except FileNotFoundError:
    print(f"\nError: File '{file_path}' not found in the specified folder")
except Exception as e:
    print(f"\nAn error occurred: {e}")

# Load the data into a DataFrame
file_path = "case_study_data_2025-01-16T06_49_12.19881Z.csv"
df = pd.read_csv(file_path)

# Display basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

print("\nDataFrame Shape:")
print(df.shape)

print("\nFirst few rows:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicate rows:")
print(f"Number of duplicate rows: {df.duplicated().sum()}")
if df.duplicated().sum() > 0:
    print("\nExample of duplicate rows:")
    print(df[df.duplicated(keep='first')])

# Check for inconsistencies in categorical columns
print("\nUnique values in each column:")
for column in df.select_dtypes(include=['object']).columns:
    print(f"\n{column}:")
    print(df[column].value_counts())
    # Check for leading/trailing whitespace or case inconsistencies
    if df[column].str.strip().ne(df[column]).any() or \
       df[column].str.lower().ne(df[column].str.strip()).any():
        print(f"Warning: Possible inconsistencies in {column}")

# Check for outliers in numerical columns
print("\nOutlier Analysis:")
numeric_columns = df.select_dtypes(include=[np.number]).columns

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
    
    print(f"\n{column}:")
    print(f"Number of outliers: {len(outliers)}")
    if len(outliers) > 0:
        print(f"Outlier values: \n{outliers.head()}")
    
    # Create box plot for visualization
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.show()

# Basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Check for any missing values
print("\nMissing values:")
print(df.isnull().sum())

Create the following columns: “Month-Year” (e.g., August 2024) from the “DATE” column. 

