# 🧬 Epigenetic ML Model  
Machine learning pipeline predicting health-related outcomes from DNA methylation (epigenetic) features.  
Includes preprocessing, feature engineering, regression modeling, and evaluation.

---

## 📌 Overview  
This project implements a clean, modular ML workflow commonly used in computational biology and bioinformatics research.  
It follows a full pipeline:

1. **Load & clean epigenetic feature data**  
2. **Handle missing values and scale features**  
3. **Train a regression model (Ridge Regression)**  
4. **Evaluate model performance (MSE)**  
5. **Save model + scaler for reuse**

This project demonstrates skills relevant for **machine learning**, **bioinformatics**, **data science**, and **quantitative research**.

---

## 📂 Project Structure

epigenetic-ml-model/
│
├── data/
│ └── your_dataset.csv # (Add your epigenetic feature dataset here)
│
├── src/
│ ├── preprocess.py # Data loading, cleaning, scaling
│ ├── train_model.py # Training + saving model + scaler
│ └── evaluate.py # Model evaluation on new data
│
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## 🧪 Methods

### **1. Preprocessing**
- Drops columns with excessive missing values  
- Fills remaining missing values using numeric medians  
- Splits into features (X) and target variable (y)  
- Scales features using `StandardScaler`

### **2. Model**
Uses **Ridge Regression**, ideal for biological datasets with:
- noisy features  
- correlated predictors  
- high dimensionality  

### **3. Evaluation**
Reports:
- Mean Squared Error (MSE)  
- Predictions for downstream analysis  

---

## ▶️ How to Run

### **1. Install dependencies**
```bash
pip install -r requirements.txt
```

### **2. Train the model**
```bash
python src/train_model.py
```

### **3. Evaluate the model**
```bash
python src/evaluate.py
```


