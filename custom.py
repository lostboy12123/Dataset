import pandas as pd
import numpy as np

# Create sample data
data = {
    'group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'value1': [10, 20, 15, 25, 30, 35],
    'value2': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Define a custom aggregation function
def range_and_mean(x):
    return pd.Series({
        'range': x.max() - x.min(),
        'mean': x.mean()
    })

# Apply the custom aggregation
result = df.groupby('group').apply(lambda g: pd.Series({
    'value1_range': g['value1'].max() - g['value1'].min(),
    'value1_mean': g['value1'].mean(),
    'value2_sum': g['value2'].sum()
}))

print("Original Data:")
print(df)
print("\
Custom Aggregation Result:")
print(result)