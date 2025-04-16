# 🚀 Customer Churn Prediction | Logistic Regression + Streamlit App

## 📌 Project Summary

This project aims to predict **customer churn** using logistic regression—a critical classification problem for businesses looking to improve customer retention. Built with Python and deployed as an interactive **Streamlit web application**, this project demonstrates end-to-end machine learning: from data preprocessing and model training to real-time prediction.

Whether you're an ML enthusiast or a hiring manager, this project showcases a clear application of data science for real-world business impact.

---

## 🧠 Key Highlights

- 🔍 **Binary Classification** using **Logistic Regression**
- 📊 **Exploratory Data Analysis (EDA)** to understand churn behavior
- 🧼 **Feature Engineering** and preprocessing (scaling, encoding)
- 🧠 Real-time predictions via **Streamlit web app**
- 🧪 Model persistence using **joblib**
- ✅ Production-ready structure & clean code for easy extension

---

## 🧾 Dataset

The model is trained on a structured customer churn dataset containing:
- `Age`
- `Monthly Charges`
- `Tenure`
- `Gender`
- `Churn` (Target)

All data preprocessing steps (scaling and encoding) are applied before modeling to maintain consistency during inference.

---

## 📁 Project Structure

```plaintext
📦 customer-churn-prediction
├── app.py              # Streamlit app for real-time prediction
├── churn.ipynb         # EDA and model development notebook
├── model.pkl           # Trained logistic regression model
├── scaler.pkl          # StandardScaler used for preprocessing
├── requirements.txt    # Project dependencies
└── README.md           # You’re reading it!
