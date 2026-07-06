# 💳 CreditWise – Credit Score Classification System

CreditWise is an end-to-end machine learning web application that predicts a customer's credit score category as **Good**, **Standard**, or **Poor** based on financial and demographic information.

The project covers the complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, model comparison, prediction, and storage of prediction history using SQLite.

---

## 🚀 Features

- Predicts credit score categories: **Good, Standard, and Poor**
- Cleans and preprocesses a real-world financial dataset
- Performs exploratory data analysis (EDA)
- Trains and compares multiple classification models
- Evaluates models using Accuracy, Precision, Recall, and F1 Score
- Displays a confusion matrix and classification report
- Uses the best-performing model for real-time predictions
- Stores prediction records in an SQLite database
- Provides a web interface built with Flask

---

## 🧠 Machine Learning Models

The following classification algorithms were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|------|---------:|----------:|-------:|---------:|
| Logistic Regression | 29.0% | 61.6% | 29.0% | 13.1% |
| Decision Tree | 67.5% | 67.5% | 67.5% | 67.5% |
| Random Forest | **78.6%** | **78.6%** | **78.6%** | **78.6%** |

**Random Forest** achieved the best overall performance and was selected as the final model for deployment.

---

## 📊 Random Forest Performance

The final model achieved:

- **Accuracy:** 78.6%
- **Weighted Precision:** 0.79
- **Weighted Recall:** 0.79
- **Weighted F1 Score:** 0.79

The model showed balanced performance across all three credit score categories.

---

## 🔍 Exploratory Data Analysis

The project includes visual analysis of:

- Credit Score Distribution
- Customer Age Distribution
- Annual Income Distribution
- Outstanding Debt by Credit Score
- Delay from Due Date by Credit Score
- Correlation between numerical financial features

EDA revealed clear relationships between credit score categories and financial behaviour, particularly outstanding debt and payment delays.

---

## 🧹 Data Preprocessing

The original dataset contained missing values, invalid placeholders, incorrect data types, and unrealistic values.

The preprocessing pipeline includes:

- Removing unnecessary identifier columns
- Replacing invalid placeholder values
- Converting numerical columns stored as text
- Handling unrealistic values
- Converting credit history age into total months
- Filling numerical missing values using the median
- Filling categorical missing values using the mode
- Encoding categorical features using Label Encoding

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

### Web Application
- Flask
- HTML
- CSS

### Database
- SQLite

---

## 📁 Project Structure

```text
Credit-Scoring-System/
│
├── app.py
├── database.py
├── database.db
│
├── dataset/
│   ├── train.csv
│   └── test.csv
│
├── cleaned_data/
│   └── train_cleaned.csv
│
├── model/
│   ├── 01_data_preprocessing.ipynb
│   └── 02_model_training.ipynb
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── database.html
│
├── credit_model.joblib
├── label_encoders.joblib
│
└── README.md
