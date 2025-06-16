import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    data = {
        "attendance": [90, 45, 70, 30, 85, 50, 60, 95, 40, 65],
        "avg_score": [88, 40, 65, 35, 90, 50, 55, 92, 45, 60],
        "assignments_completed": [10, 2, 6, 1, 9, 3, 5, 10, 2, 6],
        "at_risk": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    X = df[["attendance", "avg_score", "assignments_completed"]]
    y = df["at_risk"]
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "risk_model.pkl")

def load_model():
    if not os.path.exists("risk_model.pkl"):
        train_model()
    return joblib.load("risk_model.pkl")