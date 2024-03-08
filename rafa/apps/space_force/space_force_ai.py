import streamlit as st
import requests
import os

st.title('Chat Engine')

st.sidebar.header('My space')

with st.sidebar.expander("Data"):
   st.write("""
      - Research_paper_1
      - Research_paper_2
   """)

with st.sidebar.expander("Assistants"):
   st.write("""
      - Agent 1
      - Agent 2
   """)

user_input = st.text_input("Enter your query:")

uploaded_file = st.sidebar.file_uploader("Upload File", type=["txt", "csv", "xlsx", "pdf"])

if uploaded_file is not None:
   # Process the uploaded file
   file_contents = uploaded_file.read()
   selected_file_name = uploaded_file.name
   st.write("Selected file name:", selected_file_name)
   # Add your code here to process the file further

   # Save the uploaded file
   file_name = selected_file_name
   file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
   os.makedirs(os.path.dirname(file_path), exist_ok=True)
   with open(file_path, "wb") as f:
      f.write(file_contents)
   st.write("File saved successfully!")

# if st.button('Send'):
#     response = requests.post('http://localhost:8000/query', json={'text': user_input})
#     print("response content is this:", response.text)
#     st.write(response.text)
