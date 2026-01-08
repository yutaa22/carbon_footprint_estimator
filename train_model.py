import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("carbon_footprint.csv")

# Encode diet_type
le = LabelEncoder()
data["diet_type"] = le.fit_transform(data["diet_type"])

# Features and target
X = data[["electricity_kwh", "fuel_liters", "transport_km", "diet_type"]]
y = data["carbon_kg"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "carbon_model.pkl")
joblib.dump(le, "diet_encoder.pkl")

print("Model trained and saved successfully")
