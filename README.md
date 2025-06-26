# ChurnGuard: Customer Churn Prediction Dashboard

ChurnGuard is a data analysis and machine learning project that predicts customer churn based on service usage patterns and demographics. It includes a trained classification model and an interactive dashboard built using Streamlit, allowing businesses to analyze churn risk for individual customers.

## Features

- Data preprocessing and exploratory data analysis (EDA)
- Customer churn prediction using Random Forest
- Interactive dashboard for live churn prediction
- Clean and modular project structure
- Easily extendable for future improvements

## Dataset

The dataset used is the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle, which includes information about customer demographics, account details, and services used.

## Directory Structure

ChurnGuard/
│
├── data/
│ └── telco_churn.csv # Raw dataset
│
├── models/
│ └── churn_model.pkl # Trained ML model
│
├── app/
│ └── app.py # Streamlit dashboard script
│
├── train_model.py # Model training and evaluation
├── requirements.txt # Python dependencies
├── screenshot.png # Dashboard screenshot
└── README.md

## How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/Bindiathayumanavan/ChurnGuard-Customer-Churn-Prediction-Dashboard.git
   cd ChurnGuard-Customer-Churn-Prediction-Dashboard
2.Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3.Install the dependencies:
   pip install -r requirements.txt
4.Train the model (if not already trained):
   python3 train_model.py
5.Run the Streamlit app:
   streamlit run app/app.py

Model Performance

Accuracy: ~78%
Classification Report:
Precision: 82% for non-churn, 63% for churn
Recall: 90% for non-churn, 45% for churn
Tech Stack

Python
Pandas, NumPy, scikit-learn
Streamlit
Matplotlib, Seaborn
