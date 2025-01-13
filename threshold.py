import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib  # Import for loading the model
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error, r2_score, f1_score, accuracy_score, precision_recall_curve
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'dataset.csv'  # Replace with your file's path
df = pd.read_csv(file_path)

# Calculate the 'Previous Metric'
df['Previous Metric'] = df['Metric'].shift(1)

# Drop rows with NaN values resulting from the shift
df.dropna(inplace=True)

# Define features (X) and target (y)
X = df[['Metric', 'Previous Metric']]
y = df['Anomaly']

# Split the data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Load the pre-trained SVM model
model_path = 'svm_model.joblib'  # Replace with your saved model's path
model = joblib.load(model_path)

# Make predictions on the test set
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred_binary = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_binary)
f1 = f1_score(y_test, y_pred_binary)

print("Accuracy:", accuracy)
print("F1 Score:", f1)

# Precision-Recall Curve
prec, rec, thresholds = precision_recall_curve(y_test, y_pred_proba)
f1_scores = 2 * (prec * rec) / (prec + rec + 1e-9)
best_idx = np.argmax(f1_scores)
best_thres = thresholds[best_idx]

print("Best Threshold:", best_thres)
print("Best F1 Score:", f1_scores[best_idx])

# Plot y_pred vs y_test
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_proba, color='blue', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, color='red')
plt.axhline(y=best_thres, color='green', linestyle='--', linewidth=2, label='y = best_thres')

plt.title('Predicted Probabilities vs True Values')
plt.xlabel('True Values (y_test)')
plt.ylabel('Predicted Probabilities (y_pred_proba)')
plt.grid(True)
plt.show()
