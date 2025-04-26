# 🚀 Customer Churn Prediction | Logistic Regression + Streamlit App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-green.svg)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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


📦 customer-churn-prediction
├── app.py              # Streamlit app for real-time prediction
├── churn.ipynb         # EDA and model development notebook
├── model.pkl           # Trained logistic regression model
├── scaler.pkl          # StandardScaler used for preprocessing
├── requirements.txt    # Project dependencies
└── README.md           # You’re reading it!

---
## 🛠 Tech Stack

| Area               | Tools Used                     |
|--------------------|--------------------------------|
| Programming        | Python 3.8+                    |
| Data Manipulation  | Pandas, NumPy                  |
| Visualization      | Seaborn, Matplotlib            |
| Modeling           | scikit-learn (LogisticRegression) |
| App Development    | Streamlit                      |
| Model Serialization| joblib                         |

## 📊 Model Performance

| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.82  |
| Precision | 0.79  |
| Recall    | 0.76  |
| F1-Score  | 0.77  |
| AUC-ROC   | 0.85  |

*The model was evaluated using 5-fold cross-validation*

## 🧪 How It Works

### 1. Clone the Repository

git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
### 2. Set up the environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
### 3. Launch the app
streamlit run app.py

## 🧮 Logistic Regression Model

    Simple yet effective baseline model

    Trained on scaled, encoded features

    Evaluated using Accuracy, Precision, Recall, F1-Score

## ✅ Why Logistic Regression?
It offers interpretability, fast training, and often serves as a solid benchmark model for classification tasks.
## 🖥️ Streamlit Web App Preview

The app accepts four inputs:

    Age (numerical)

    Monthly Charges (numerical)

    Gender (dropdown: Male/Female)

    Tenure (numerical)

Click the Predict button and get a real-time prediction:

    “🔮 The customer is predicted to churn: Yes/No”

## 📈 Future Improvements

    🔄 Add more features (e.g., internet usage, payment method, contract type)

    🌲 Test advanced models (Random Forest, XGBoost)

    🧠 Add deep learning model with PyTorch

    ☁️ Deploy the app on Render, Heroku, or AWS


## 🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.