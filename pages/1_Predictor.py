import streamlit as st
import pickle

# Set the title of the app
st.title('House Price Predictor')

# Dropdown for selecting house type
house_type = st.selectbox('Select the type of house:', ['House', 'Flat'])

# Display the predicted price (placeholder)
st.text('Price of the house would be: $XXX')  # Replace $XXX with actual prediction logic


with open('model.pkl', 'rb') as m:
    model = pickle.load(m)

with open('data.pkl', 'rb') as d:
    data = pickle.load(d)

st.dataframe(data)