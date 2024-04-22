import streamlit as st
import requests
import json
import os

def query_response(query_text):
    response = requests.post('http://localhost:8000/query', json={'text': query_text})
    print("response content is this:", response.text)
    response_json = json.loads(response.text)
    response_text = response_json['response']
    response_text = response_text.replace("\\n", "\n")
    return response

def chat_response(query_text):
    response = requests.post('http://localhost:8000/query', json={'text': query_text})
    print("chat response content is this:", response.text)
    response_json = json.loads(response.text)
    response_text = response_json['response']
    response_text = response_text.replace("\\n", "\n")
    return response_text

st.title('Friday')

# Create two columns
left_column, right_column = st.columns(2)

# Left column for file viewer
with left_column:
    # Add your file viewer code here

    # Get the list of .pdf files in the 'data' directory
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    pdf_files = [file for file in os.listdir(data_dir) if file.endswith('.pdf')]

    # Create a dropdown box to select the file
    selected_file = st.selectbox("Select a PDF file", pdf_files)

    # Read and display the selected file
    # if selected_file:
    #     file_path = os.path.join(data_dir, selected_file)
    #     with open(file_path, 'rb') as file:
    #         st.write(file.read())
    # st.write("File Viewer")

# Right column for chat engine
with right_column:
    st.header("Chat with Friday 💬 📚")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # response = f"Echo: {query_response(prompt)}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Thinking!"):
                response = chat_response(prompt)
                st.write(response)
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)