import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have your dataset loaded into a pandas DataFrame 'dataset'
# Replace 'iris.csv' with your file path
dataset = pd.read_csv('iris.csv')

X = dataset.iloc[:, :-1].values  # Selecting all columns except the last as features
y = dataset.iloc[:, -1].values   # Selecting the last column as the target

# Displaying the first 5 rows of the dataset
print(dataset.head(5))

from sklearn.model_selection import train_test_split

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()

# Training the classifier
classifier.fit(X_train, y_train)

# Predicting on the test set
y_pred = classifier.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix, accuracy_score

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Accuracy score
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Creating a DataFrame to display real vs predicted values
df = pd.DataFrame({'Real Values': y_test, 'Predicted Values': y_pred})
print(df)
