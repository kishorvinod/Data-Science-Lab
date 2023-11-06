import pandas as pd

# i) Read the 'iris' dataset
iris_data = pd.read_csv('iris.csv')  # Replace 'iris.csv' with the actual file path if needed

# ii) Display Shape of the dataset
shape = iris_data.shape
print("Shape of the dataset:", shape)

# iii) First 5 and last 5 rows of the dataset (head and tail)
print("First 5 rows of the dataset:")
print(iris_data.head(5))
print("\nLast 5 rows of the dataset:")
print(iris_data.tail(5))

# iv) Size of the dataset
size = iris_data.size
print("\nSize of the dataset:", size)

# v) Number of samples available for each variety
variety_counts = iris_data['variety'].value_counts()
print("\nNumber of samples for each variety:")
print(variety_counts)

# vi) Description of the dataset (use describe)
description = iris_data.describe()
print("\nDescription of the dataset:")
print(description)
