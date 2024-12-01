# First, let's read and examine the data
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Read the CSV file
df = pd.read_csv('100_Sales.csv')

# Display initial info about the dataset
print("Initial dataset info:")
print(df.info())
print("\
Sample of data:")
print(df.head())

# Re-importing necessary libraries and loading the dataset
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Read the CSV file
df = pd.read_csv('100_Sales.csv')

# Display initial info about the dataset
print("Initial dataset info:")
print(df.info())
print("\
Sample of data:")
print(df.head())

# Let's perform some data cleaning and deduplication

# 1. Clean up whitespace in string columns
string_columns = df.select_dtypes(include=['object']).columns
df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())

# 2. Standardize text case in categorical columns
categorical_columns = ['Region', 'Country', 'Item_Type', 'Sales_Channel', 'Order_Priority']
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.str.title())

# 3. Check for potential duplicates using fuzzy matching on Country names
# Get unique countries
unique_countries = df['Country'].unique()

# Create a dictionary to store similar country names
similar_countries = {}
for country1 in unique_countries:
    for country2 in unique_countries:
        if country1 != country2:
            ratio = fuzz.ratio(country1.lower(), country2.lower())
            if ratio > 80:  # threshold for similarity
                similar_countries[f"{country1} - {country2}"] = ratio

print("Potential similar country names (similarity > 80%):")
for pair, ratio in similar_countries.items():
    print(f"{pair}: {ratio}%")

# 4. Check for exact duplicates
duplicate_count = df.duplicated().sum()
print(f"\
Number of exact duplicates found: {duplicate_count}")

# 5. Basic statistics after cleaning
print("\
Basic statistics after cleaning:")
print(df.describe())

# Resolving fuzzy matches for 'Australia' and 'Austria'
# Replace 'Austria' with 'Australia' for consistency

def resolve_fuzzy_matches(row):
    if row['Country'] == 'Austria':
        return 'Australia'
    return row['Country']

df['Country'] = df.apply(resolve_fuzzy_matches, axis=1)

# Verify changes
print("Updated unique country names:")
print(df['Country'].unique())