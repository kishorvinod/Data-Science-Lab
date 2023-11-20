import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('car_details.csv')

# Assuming 'Label' is the target variable
X = data.drop('Label', axis=1)
y = data['Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Predict classes for the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Decision Tree Classifier: {accuracy}")

# Find mislabeled classifications
mislabeled = (y_test != y_pred).sum()
print(f"Number of mislabeled classifications: {mislabeled}")

# List class labels of mismatching records
mismatched_indices = [i for i, (actual, pred) in enumerate(zip(y_test, y_pred)) if actual != pred]
mismatched_labels = [y_test.iloc[i] for i in mismatched_indices]
print(f"Class labels of mismatching records: {mismatched_labels}")
