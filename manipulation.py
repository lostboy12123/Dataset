# This code creates a custom numpy data type and uses it in an array.
import numpy as np

# Define a custom numpy data type for a structured array
# Example: A data type for a person with name (string), age (integer), and height (float)
person_dtype = np.dtype([
    ('name', 'U10'),  # String of max length 10
    ('age', 'i4'),    # 4-byte integer
    ('height', 'f4')  # 4-byte float
])

# Create an array of this custom data type
people = np.array([
    ('Alice', 25, 5.5),
    ('Bob', 30, 6.0),
    ('Charlie', 35, 5.8)
], dtype=person_dtype)

# Print the array and its data type
print("Array:")
print(people)
print("\
Data Type:")
print(people.dtype)