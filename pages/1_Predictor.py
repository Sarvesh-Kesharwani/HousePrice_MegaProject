import streamlit as st
import pickle
import pandas as pd

# Set the title of the app
st.title('House Price Predictor')

with open(r'model.pkl', 'rb') as m:
    model = pickle.load(m)

data = pd.read_csv(r'data.csv')
# data.drop(['Unnamed: 0'], axis=1, inplace=True)
st.dataframe(data)

# property_type
property_type = st.selectbox('Property Type', ['flat', 'house'])

# sector
sector = st.selectbox('Sector', data['sector'].unique().tolist())

# floorNum
floorNum = st.selectbox('floorNum', data['floorNum'].unique().tolist())

# sector
# st.selectbox('Sector', data['sector'].unique().tolist())

# sector
# st.selectbox('Sector', data['sector'].unique().tolist())


data = [[]]
columns = ['price_per_sqft', 'floorNum',
       'property_type', 'noOfFloor', 'SuperBuiltupArea_sqft',
       'BuiltupArea_sqft', 'CarpetArea_sqft', 'servantRoom', 'studyRoom',
       'poojaRoom', 'storeRoom', 'otherAdditionalRoom', 'luxury_class']

# Display the predicted price (placeholder)
if st.button('Predict'):
    # form a dataframe
    
    # predict
    predicted_price = model.predict()
    
    # display the price
    st.text(predicted_price)
