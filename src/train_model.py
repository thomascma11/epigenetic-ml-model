import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import joblib

from preprocess import load_data, preprocess


def train_model(data_path, model_out="model.pkl", scaler_out="scaler.pkl"):
    # Load raw dataset
    df = load_data(data_path)

    # Preprocess (clean + scale)
    X, y, scaler = preprocess(df)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Ridge Regression (robust + widely used)
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    print("Model trained.")
    print(f"Validation MSE: {mse:.4f}")

    # Save model + scaler
    joblib.dump(model, model_out)
    joblib.dump(scaler, scaler_out)

    return model, scaler, mse


if __name__ == "__main__":
    # Example run
    train_model("data/epigenetic_data.csv")
