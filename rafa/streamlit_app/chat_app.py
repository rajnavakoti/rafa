import streamlit as st
import requests

st.title('Chat Engine')

user_input = st.text_input("Enter your query:")

if st.button('Send'):
    response = requests.post('http://localhost:8000/query', json={'text': user_input})
    print("response content is this:", response.text)
    st.write(response.text)