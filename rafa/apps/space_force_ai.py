import streamlit as st
import requests

st.title('Chat Engine')

# st.sidebar.image('dev_problem.png', use_column_width=True)
st.sidebar.text('Chat Engine')

with st.sidebar.expander("Data sources"):
     st.write("""
        - Research_paper_1
        - Research_paper_2
     """)

with st.sidebar.expander("Agents"):
     st.write("""
        - Agent 1
        - Agent 2
     """)

st.sidebar.subheader('Settings')

user_input = st.text_input("Enter your query:")

# if st.button('Send'):
#     response = requests.post('http://localhost:8000/query', json={'text': user_input})
#     print("response content is this:", response.text)
#     st.write(response.text)