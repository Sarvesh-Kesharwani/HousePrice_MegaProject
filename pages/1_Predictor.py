import streamlit as st
import pickle
import pandas as pd

# Set the title of the app
st.title('House Price Predictor')

# Dropdown for selecting house type
house_type = st.selectbox('Select the type of house:', ['House', 'Flat'])

# Display the predicted price (placeholder)
st.text('Price of the house would be: $XXX')  # Replace $XXX with actual prediction logic


with open(r'model.pkl', 'rb') as m:
    model = pickle.load(m)

data = pd.read_csv(r'final_data.csv')
st.dataframe(data)

# property_type
st.selectbox('Property Type', ['flat', 'house'])

# sector
st.selectbox('Sector', data['sector'])