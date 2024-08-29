import streamlit as st


# Set the title of the app
st.title('Check which feature of your next house will cost you more')

# Dropdown for selecting house type
house_type = st.selectbox('Select the type of house:', ['House', 'Flat'])

# Display the predicted price (placeholder)
st.text('Price of the house would be: $XXX')  # Replace $XXX with actual prediction logic
