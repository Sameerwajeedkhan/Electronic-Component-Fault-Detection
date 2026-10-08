import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA = "data/electronic_components.csv"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(DATA)
features = ["Voltage", "Current", "Resistance", "Temperature", "Frequency", "Vibration"]
X = df[features]
y = df["Fault"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=["Normal", "Faulty"]))
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))

joblib.dump(model, os.path.join(MODEL_DIR, "fault_detector.pkl"))
print("\nModel saved to models/fault_detector.pkl")
