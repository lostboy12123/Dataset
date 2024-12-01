# Import necessary libraries
import pandas as pd
from fuzzywuzzy import fuzz, process

# Load the dataset
df = pd.read_csv('tested.csv')

# Display the first few rows to understand the structure of the data
print(df.head())
print(df.info())

# Perform fuzzy string matching for deduplication based on the 'Name' column
from tqdm import tqdm

def find_duplicates(df, column, threshold=90):
    """
    Identifies potential duplicates in a dataframe column using fuzzy string matching.
    
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        column (str): The column to check for duplicates.
        threshold (int): The similarity threshold for considering two strings as duplicates.

    Returns:
        list: A list of tuples containing the indices of potential duplicates.
    """
    duplicates = []
    checked = set()
    
    for i, name in tqdm(enumerate(df[column]), total=len(df[column])):
        if name not in checked:
            matches = process.extract(name, df[column], scorer=fuzz.ratio)
            for match in matches:
                if match[1] >= threshold and match[0] != name:
                    duplicates.append((i, df[df[column] == match[0]].index[0]))
            checked.add(name)
    return duplicates

# Find duplicates in the 'Name' column
duplicates = find_duplicates(df, 'Name')

# Display the duplicates found
print("Potential duplicates found:", duplicates)

# Let's also clean up other aspects of the data

# 1. Handle missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing ages with median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing cabin with 'Unknown'
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\
Missing values after cleaning:")
print(df.isnull().sum())

# 2. Standardize text data
df['Sex'] = df['Sex'].str.lower()
df['Embarked'] = df['Embarked'].str.upper()

# 3. Remove any leading/trailing whitespace
df['Name'] = df['Name'].str.strip()

# Display sample of cleaned data
print("\
Sample of cleaned data:")
print(df.head())
