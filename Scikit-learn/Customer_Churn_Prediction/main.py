# ============================================
# CUSTOMER CHURN PREDICTION
# Step 1: Load and understand the dataset
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV dataset
df = pd.read_csv("Telco-Customer-Churn.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display number of rows and columns
print("\nShape of the dataset:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns)

# Display information about the dataset
print("\nDataset information:")
print(df.info())
# ============================================
# Step 2: Check data quality
# ============================================

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check unique values in the target column
print("\nUnique values in Churn:")
print(df["Churn"].unique())

# Check the number of customers in each churn category
print("\nChurn distribution:")
print(df["Churn"].value_counts())
# ============================================
# Step 3: Clean the TotalCharges column
# ============================================

# Convert TotalCharges from object to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check if conversion created missing values
print("\nMissing values after converting TotalCharges:")
print(df["TotalCharges"].isnull().sum())

# Remove rows where TotalCharges is missing
df.dropna(subset=["TotalCharges"], inplace=True)

# Check the new shape
print("\nShape after cleaning:")
print(df.shape)

# Check the data type
print("\nData type of TotalCharges:")
print(df["TotalCharges"].dtype)
# ============================================
# Step 4: Exploratory Data Analysis
# ============================================

# 1. Churn distribution
plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Churn")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 2. Churn based on contract type
plt.figure(figsize=(7, 4))

sns.countplot(data=df, x="Contract", hue="Churn")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 3. Churn based on customer tenure
plt.figure(figsize=(7, 4))

sns.boxplot(data=df, x="Churn", y="tenure")

plt.title("Customer Churn vs Tenure")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.show()

# ============================================
# Step 5: Prepare data for Machine Learning
# ============================================

# Remove customerID because it is only an identifier
df.drop("customerID", axis=1, inplace=True)

# Convert Churn into numerical values
# No = 0, Yes = 1
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# Separate features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nShape of X:")
print(X.shape)

print("\nShape of y:")
print(y.shape)

# ============================================
# Step 6: Encode categorical features
# ============================================

# Convert categorical columns into numerical columns
X = pd.get_dummies(X, drop_first=True)

print("\nShape of X after encoding:")
print(X.shape)

print("\nFirst 5 rows after encoding:")
print(X.head())

# ============================================
# Step 7: Train-Test Split
# ============================================

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data shape:")
print(X_train.shape)

print("\nTesting data shape:")
print(X_test.shape)

print("\nTraining target shape:")
print(y_train.shape)

print("\nTesting target shape:")
print(y_test.shape)
# ============================================
# Step 8: Train Logistic Regression Model
# ============================================

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create a StandardScaler
scaler = StandardScaler()

# Fit scaler only on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform testing data using the same scaler
X_test_scaled = scaler.transform(X_test)

# Create Logistic Regression model
logistic_model = LogisticRegression(max_iter=2000)

# Train the model
logistic_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_logistic = logistic_model.predict(X_test_scaled)

# Calculate accuracy
logistic_accuracy = accuracy_score(y_test, y_pred_logistic)

print("\nLogistic Regression Accuracy:")
print(logistic_accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_logistic))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_logistic))

# ============================================
# Step 9: Decision Tree Classifier
# ============================================

from sklearn.tree import DecisionTreeClassifier

# Create the Decision Tree model
decision_tree = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

# Train the model
decision_tree.fit(X_train, y_train)

# Make predictions
y_pred_tree = decision_tree.predict(X_test)

# Calculate accuracy
tree_accuracy = accuracy_score(y_test, y_pred_tree)

print("\nDecision Tree Accuracy:")
print(tree_accuracy)

# Classification report
print("\nDecision Tree Classification Report:")
print(classification_report(y_test, y_pred_tree))

# Confusion matrix
print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_tree))

# ============================================
# Step 10: Random Forest Classifier
# ============================================

from sklearn.ensemble import RandomForestClassifier

# Create the Random Forest model
random_forest = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

# Train the model
random_forest.fit(X_train, y_train)

# Make predictions
y_pred_forest = random_forest.predict(X_test)

# Calculate accuracy
forest_accuracy = accuracy_score(y_test, y_pred_forest)

print("\nRandom Forest Accuracy:")
print(forest_accuracy)

# Classification report
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_forest))

# Confusion matrix
print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_forest))
# ============================================
# Step 12: Compare Model Performance
# ============================================

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest"
]

accuracies = [
    logistic_accuracy,
    tree_accuracy,
    forest_accuracy
]

plt.figure(figsize=(8, 5))

plt.bar(models, accuracies)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy")

# Display accuracy values above bars
for i, accuracy in enumerate(accuracies):
    plt.text(i, accuracy + 0.01, f"{accuracy:.2%}", ha="center")

plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# ============================================
# Step 13: Logistic Regression Confusion Matrix
# ============================================

plt.figure(figsize=(6, 5))

sns.heatmap(
    confusion_matrix(y_test, y_pred_logistic),
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Churn", "Churn"],
    yticklabels=["No Churn", "Churn"]
)

plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()
plt.show()
# ============================================
# Step 14: Predict Churn for a New Customer
# ============================================

# Create information for a new customer
new_customer = pd.DataFrame({
    "gender": ["Female"],
    "SeniorCitizen": [0],
    "Partner": ["No"],
    "Dependents": ["No"],
    "tenure": [5],
    "PhoneService": ["Yes"],
    "MultipleLines": ["No"],
    "InternetService": ["Fiber optic"],
    "OnlineSecurity": ["No"],
    "OnlineBackup": ["No"],
    "DeviceProtection": ["No"],
    "TechSupport": ["No"],
    "StreamingTV": ["Yes"],
    "StreamingMovies": ["Yes"],
    "Contract": ["Month-to-month"],
    "PaperlessBilling": ["Yes"],
    "PaymentMethod": ["Electronic check"],
    "MonthlyCharges": [85.50],
    "TotalCharges": [427.50]
})

# Convert categorical values into the same encoded format
new_customer_encoded = pd.get_dummies(new_customer, drop_first=True)

# Make sure the new customer has exactly the same columns as training data
new_customer_encoded = new_customer_encoded.reindex(
    columns=X.columns,
    fill_value=0
)

# Scale the new customer using the scaler already fitted on training data
new_customer_scaled = scaler.transform(new_customer_encoded)

# Make prediction
new_prediction = logistic_model.predict(new_customer_scaled)[0]

# Display the result
print("\n============================================")
print("NEW CUSTOMER CHURN PREDICTION")
print("============================================")

if new_prediction == 1:
    print("Prediction: CUSTOMER IS LIKELY TO CHURN")
else:
    print("Prediction: CUSTOMER IS LIKELY TO STAY")


