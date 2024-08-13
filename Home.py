import streamlit as st 
import pandas as pd 
import st_pages

# setting page config at the beggining
st.set_page_config(
    page_title='House Price',
    page_icon='',
    layout='centered',
    initial_sidebar_state='auto'
)

if __name__ == '__main__':
    st.title('Homepage')
    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input('pick a number', 0, 10)
    with col2:
        x2 = st.number_input('pick another number', 0, 10)

    st.button('Multiply!', type='primary')


