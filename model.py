import argparse
import joblib
import numpy as np
import sys

# Load the pre-trained model from the file
model_file = "/home/cell/flexric/build/examples/xApp/c/monitor/anomaly_detector/svm_model.joblib"  # Path to the saved model file
loaded_model = joblib.load(model_file)
# print("Model loaded successfully.")

# Define the best threshold
best_thresh = 0.22687424501464445

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Predict if the input metrics indicate an anomaly.")
parser.add_argument("previous_metric", type=float, help="The previous metric value")
parser.add_argument("actual_metric", type=float, help="The actual metric value")

args = parser.parse_args()
previous_metric = args.previous_metric
actual_metric = args.actual_metric

print("Previous metric:", previous_metric)
print("Actual metric:", actual_metric)

# Prepare the input features for prediction
input_features = np.array([[actual_metric, previous_metric]])  # Format: [[Metric, Previous Metric]]

# Predict probability of anomaly
y_pred_proba = loaded_model.predict_proba(input_features)[:, 1][0]  # Get probability for class 1 (anomaly)

# Apply the best threshold to classify as anomaly or not
is_anomaly = y_pred_proba >= best_thresh

if is_anomaly:
    print("Anomaly detected!")
else:
    print("No anomaly detected.")