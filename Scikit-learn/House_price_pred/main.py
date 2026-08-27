# Importing required libraries
import numpy as np
import pandas as pd


# ============================================================
# Loading Dataset
# ============================================================

dataset = pd.read_csv("kc_house_data_without_id_date.csv")

print(dataset.head())

# ============================================================
# Handling Missing Values
# ============================================================

print("-" * 80)
print("Missing values before handling:")

print(dataset.isnull().sum())


# Remove rows where price is missing
dataset = dataset.dropna(subset=["price"])


# Fill missing values in numerical columns
dataset = dataset.fillna(dataset.median(numeric_only=True))


print("-" * 80)
print("Missing values after handling:")

print(dataset.isnull().sum())


# ============================================================
# Selecting Features (X) and Target (y)
# ============================================================

# X = input features
# y = price that we want to predict

X = dataset.drop("price", axis=1).values
y = dataset["price"].values


# Display shape of data
print("-" * 80)

print(f"Shape of X is {X.shape}")
print(f"Shape of y is {y.shape}")


# ============================================================
# Splitting Dataset into Training and Testing Sets
# ============================================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)


print("-" * 80)

print(f"Length of X_train: {len(X_train)}")
print(f"Length of X_test: {len(X_test)}")

print(f"Length of y_train: {len(y_train)}")
print(f"Length of y_test: {len(y_test)}")


# ============================================================
# Feature Scaling
# ============================================================

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()


# Fit scaler only on training data
X_train = sc.fit_transform(X_train)


# Transform test data using the same scaler
X_test = sc.transform(X_test)


# ============================================================
# Evaluation Metrics
# ============================================================

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# ============================================================
# 1. Support Vector Regression (SVR)
# ============================================================

# SVR predicts continuous values such as house prices.

from sklearn.svm import SVR

classifier = SVR()

print("\n")
print("-" * 80)
print("1. SUPPORT VECTOR REGRESSION")
print("-" * 80)

print(classifier)


# Train model
classifier.fit(X_train, y_train)


# Predict test data
y_pred = classifier.predict(X_test)


# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))


# ============================================================
# 2. Linear Regression
# ============================================================

# Linear Regression finds a relationship
# between the features and house price.

from sklearn.linear_model import LinearRegression

classifier = LinearRegression()

print("\n")
print("-" * 80)
print("2. LINEAR REGRESSION")
print("-" * 80)

print(classifier)


# Train model
classifier.fit(X_train, y_train)


# Predict test data
y_pred = classifier.predict(X_test)


# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))


# ============================================================
# 3. Decision Tree Regression
# ============================================================

# Decision Tree splits data into branches
# based on feature values.

from sklearn.tree import DecisionTreeRegressor

classifier = DecisionTreeRegressor(random_state=0)

print("\n")
print("-" * 80)
print("3. DECISION TREE REGRESSION")
print("-" * 80)

print(classifier)


# Train model
classifier.fit(X_train, y_train)


# Predict test data
y_pred = classifier.predict(X_test)


# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))


# ============================================================
# 4. Random Forest Regression
# ============================================================

# Random Forest creates many decision trees
# and combines their predictions.

from sklearn.ensemble import RandomForestRegressor

random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=0
)

print("\n")
print("-" * 80)
print("4. RANDOM FOREST REGRESSION")
print("-" * 80)

print(random_forest_model)


# Train model
random_forest_model.fit(X_train, y_train)


# Predict test data
y_pred = random_forest_model.predict(X_test)


# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))


# ============================================================
# 5. K-Nearest Neighbors Regression
# ============================================================

# KNN predicts the price based on
# similar houses nearby in the dataset.

from sklearn.neighbors import KNeighborsRegressor

classifier = KNeighborsRegressor(n_neighbors=5)

print("\n")
print("-" * 80)
print("5. K-NEAREST NEIGHBORS REGRESSION")
print("-" * 80)

print(classifier)


# Train model
classifier.fit(X_train, y_train)


# Predict test data
y_pred = classifier.predict(X_test)


# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))


# ============================================================
# Predict Price of a New House
# ============================================================

print("\n")
print("=" * 80)
print("HOUSE PRICE PREDICTION")
print("=" * 80)

new_house = np.array([[
    3,          # bedrooms
    2.0,        # bathrooms
    1800,       # sqft_living
    5000,       # sqft_lot
    1.0,        # floors
    0,          # waterfront
    0,          # view
    3,          # condition
    7,          # grade
    1800,       # sqft_above
    0,          # sqft_basement
    1990,       # yr_built
    0,          # yr_renovated
    98001,      # zipcode
    47.5,       # lat
    -122.2,     # long
    1800,       # sqft_living15
    5000        # sqft_lot15
]])


# Scale the new house
new_house_scaled = sc.transform(new_house)


# Predict using Random Forest
predicted_price = random_forest_model.predict(
    new_house_scaled
)


# Display predicted price
print("-" * 80)

print("Predicted House Price:")

print(f"${predicted_price[0]:,.2f}")

print("=" * 80)
