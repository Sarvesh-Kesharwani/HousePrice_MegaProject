import streamlit as st


# Set the title of the app
st.title('Get House recommendations with the features you are looking in your house')

# Dropdown for selecting house type
house_type = st.selectbox('Select the type of house:', ['House', 'Flat'])

# Display the predicted price (placeholder)
st.text('Price of the house would be: $XXX')  # Replace $XXX with actual prediction logic
