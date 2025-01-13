import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump


# Load the dataset
file_path = 'dataset.csv'  # Replace with your file's path
df = pd.read_csv(file_path)

# Calculate the 'Previous Metric'
df['Previous Metric'] = df['Metric'].shift(1)
df['Previous result'] = df['Anomaly'].shift(1)

# Drop rows with NaN values resulting from the shift
df.dropna(inplace=True)

# Define features (X) and target (y)
X = df[['Metric', 'Previous Metric', 'Previous result']]
y = df['Anomaly']

# Split the data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the SVM model
model = SVC(probability=True, random_state=42)
model.fit(X_train, y_train)
dump(model, 'svm_model.joblib')
