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
# image = st.image('path_to_image', use_column_width=False, width=100)
st.sidebar.markdown("[datasets](#datasets)")
st.sidebar.markdown("[chat](#chat)")
st.sidebar.markdown("[documentation](#documentation)")
st.subheader("I'm an AI assistant 🧠 💬 📚")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What'sup?"):
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