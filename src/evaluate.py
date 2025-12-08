import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error

from preprocess import load_data, preprocess


def evaluate_model(data_path, model_path="model.pkl", scaler_path="scaler.pkl"):
    # Load saved model + scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Load dataset
    df = load_data(data_path)

    # Preprocess (clean + scale)
    X, y, _ = preprocess(df)

    # Apply saved scaler to features
    X_scaled = scaler.transform(X)

    # Predict
    preds = model.predict(X_scaled)

    # Compute MSE
    mse = mean_squared_error(y, preds)

    print("Evaluation complete.")
    print(f"MSE on dataset: {mse:.4f}")

    return mse, preds


if __name__ == "__main__":
    evaluate_model("data/epigenetic_data.csv")
