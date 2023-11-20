# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
# Load the dataset
glass_df = pd.read_csv("glass.csv")

# Assuming the last column is the target (label) column
X = glass_df.iloc[:, :-1]
y = glass_df.iloc[:, -1]

# Experiment with different values for test and training dataset sizes
test_sizes = [0.2, 0.3, 0.4]

# Experiment with different values for k
k_values = [3, 5, 7]

# Iterate through different test sizes and k values
for test_size in test_sizes:
    for k in k_values:
        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        # Create KNN model
        knn = KNeighborsClassifier(n_neighbors=k)

        # Fit the model on the training set
        knn.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = knn.predict(X_test)

        # Calculate accuracy
        accuracy = metrics.accuracy_score(y_test, y_pred)

        # Display the results
        print(f"Test Size = {test_size}, K = {k}, Accuracy: {accuracy:.2f}")
