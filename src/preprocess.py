import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):
    # Drop columns with too many missing values
    df = df.dropna(thresh=len(df) * 0.5, axis=1)

    # Fill remaining missing values
    df = df.fillna(df.median(numeric_only=True))

    # Separate features and target
    X = df.drop("target", axis=1)
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
