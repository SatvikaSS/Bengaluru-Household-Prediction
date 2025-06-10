# Bengaluru-Household-Prediction

A Streamlit web app that predicts house prices in Bengaluru based on features like total square feet, number of bedrooms (BHK), bathrooms, and location. The model is trained using Linear Regression on a cleaned dataset from Kaggle.

---

## 📌 Features

- Data preprocessing and feature engineering
- Trained using Linear Regression
- Location-based price prediction
- One-hot encoding for location handling
- Clean and interactive Streamlit UI
- Model and column saving using pickle

---

## 📁 Project Structure

bengaluru-house-price-predictor/
├── app.py # Streamlit web app
├── model.py # Data preprocessing + model training
├── Bengaluru_House_Data.csv # Dataset
├── bangalore_model.pkl # Trained model (output from model.py)
├── model_columns.pkl # Feature column names (used by app.py)
└── README.md # Project documentation

---

## 📊 Dataset

- Dataset used: [Bengaluru House Price Data - Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- Features considered:
  - Location
  - Total square feet
  - Number of bedrooms (BHK)
  - Number of bathrooms

---

## ⚙️ Setup Instructions

-Install Dependencies
    pip install streamlit scikit-learn pandas numpy

---
## 🔧 Steps to be followed
✅ Step 1: Train the Model
          python model.py
          
   -Cleans the dataset
   -Handles outliers
   -Encodes location
   -Trains the model and saves it to bangalore_model.pkl and model_columns.pkl

✅ Step 2: Run the Web App
          streamlit run app.py

  -Opens a browser window with input fields:
      ├──Total Square Feet
      ├──BHK
      ├──Bathrooms
      ├──Location
  -Displays predicted price in Lakhs INR

---

Acknowledgments
Kaggle Dataset: Bengaluru House Price Data

---

Output
![image](https://github.com/user-attachments/assets/fdddb9a0-df9d-4c61-bb25-56bc7db35cac)




