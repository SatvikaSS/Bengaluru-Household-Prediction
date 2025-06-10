import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('bangalore_model.pkl', 'rb'))
columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title("🏡 Bengaluru House Price Predictor")

total_sqft = st.number_input("Total Square Feet", min_value=300.0, step=10.0)
bath = st.slider("Bathrooms", 1, 10, 2)
bhk = st.slider("Bedrooms (BHK)", 1, 10, 2)

locations = [col for col in columns if col not in ['total_sqft', 'bath', 'bhk']]
location = st.selectbox("Location", sorted(locations + ['other']))

if st.button("Predict Price"):
    input_data = np.zeros(len(columns))
    input_data[columns.get_loc('total_sqft')] = total_sqft
    input_data[columns.get_loc('bath')] = bath
    input_data[columns.get_loc('bhk')] = bhk
    if location != 'other' and location in columns:
        input_data[columns.get_loc(location)] = 1

    result = model.predict([input_data])[0]
    st.success(f"Estimated Price: ₹ {round(result, 2)} Lakhs")
