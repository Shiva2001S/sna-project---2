import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data from CSV file
data = pd.read_csv('my2.csv')

# Convert data to a numpy array
data = np.array(data)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[:, :2], data[:, 2], test_size=0.2)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on test data
y_pred = model.predict(X_test)

# Compute accuracy of predictions
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
