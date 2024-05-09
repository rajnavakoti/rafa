import streamlit as st
import requests
import json
import os
from PIL import Image
import logging
from dotenv import load_dotenv

# Load and setup environment variables from .env file
load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
USER_AVATAR = os.environ.get("DOCKER_USER_AVATAR") if IS_DOCKER else os.environ.get("LOCAL_USER_AVATAR")
FRIDAY_AVATAR = os.environ.get("DOCKER_FRIDAY_AVATAR") if IS_DOCKER else os.environ.get("LOCAL_FRIDAY_AVATAR")
INTERMEDIARY_SERVER = os.environ.get("DOCKER_INTERMEDIATE_SERVER") if IS_DOCKER else os.environ.get("LOCAL_INTERMEDIATE_SERVER")
OLLAMA_SERVER = os.environ.get("DOCKER_OLLAMA_SERVER") if IS_DOCKER else os.environ.get("LOCAL_OLLAMA_SERVER")
BANNER = os.environ.get("DOCKER_BANNER") if IS_DOCKER else os.environ.get("LOCAL_BANNER")
COLLECTION_NAME = os.environ.get("COLLECTION")
LLM_MODEL = os.environ.get("DOCKER_LLM_MODEL") if IS_DOCKER else os.environ.get("LOCAL_LLM_MODEL")

try:
    # Sidebar content
    img = Image.open(BANNER)
    st.sidebar.image(img, use_column_width=False, width=350, clamp=True)
    st.sidebar.markdown('<h4 style="color: black; font-family: Courier, sans-serif; font-size: 20px; font-weight: thin; text-align: center;">THANK GOD IT\'S FRIDAY 😸 </h4>', unsafe_allow_html=True)

    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  

    use_private_data_toggle =st.sidebar.toggle('Use knowledge base', value=False, key=None, help=None, 
                      on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    
    chat_modes_toggle = st.sidebar.toggle('Chat mode', value=False, key=None, help=None, 
                      on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    chat_mode = 'chat' if chat_modes_toggle else 'qa'

    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  

    # Add a text input for the collection name
    collection_name = st.sidebar.text_input('Enter the name of the new collection')
    create_collection_button = st.sidebar.button('Create Collection')
    
    choose_your_space = st.sidebar.selectbox('Data collections 🍕', ['RaFa (default)', 'Enginnering', 'Techonology', 'People & Culture', 'Product & Design', 'Sales & Marketing', 'Strategy & Operations', 'Support & Success', 'All'])

    # Add a file uploader to your app
    uploaded_file = st.sidebar.file_uploader("Add documents to the collection", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding

    st.sidebar.markdown("[Documentation](#documentation)")

    # Title container
    title_container = st.container()
    col1, col2, col3 = st.columns([1, 5, 20])
    image = Image.open(FRIDAY_AVATAR)
    with title_container:
        with col1:
            st.image(image, width=164, clamp=True, use_column_width=False, output_format='JPEG', channels='RGB', caption=None)
        with col2:
            st.write('&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;')
        with col3:
            st.markdown(' <br/><br/>  <h4 style="color: black; font-family: Courier, sans-serif; font-size: 20px; font-weight: thin;">..not just an AI, I AM FRIDAY</h4>', unsafe_allow_html=True)


    def ask_friday(query_text, chat_mode, chat_with):
        response = requests.post(
            f'{INTERMEDIARY_SERVER}/query',
            json={'text': query_text, 'chat_mode': chat_mode, 'talk_to': chat_with, 'collection': COLLECTION_NAME}
        )
        logging.info("Chat response content: %s", response.text)
        response_text = response.json()['response'].replace("\\n", "\n")

        return response_text

    def create_collection(collection_name):
        # Add code here to create the collection
        # This is a placeholder for the implementation
        pass

    def ask_ham(query_text, chat_history, selected_chat_mode):
        try:
            if selected_chat_mode == 'qa':
                response = requests.post(
                    f'{OLLAMA_SERVER}/api/generate',
                    json={"model": LLM_MODEL, "prompt": query_text, "stream": False}
                ).json()['response'].replace("\\n", "\n")
            else:
                print({"model": LLM_MODEL, "messages": json.dumps(chat_history), "stream": False})
                response = requests.post(
                    f'{OLLAMA_SERVER}/api/chat',
                    json={"model": LLM_MODEL, "messages": chat_history, "stream": False}
                ).json()['message']['content'].replace("\\n", "\n")
            # response_text = response.json()['response'].replace("\\n", "\n")
            return response
        except Exception as e:
            st.error(f"An error occurred while calling friday or ham at line {e.__traceback__.tb_lineno}: {str(e)}")
            return "An error occurred while calling ask_ham: " + str(e)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else FRIDAY_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Add a button for creating the collection
    if create_collection_button:
    # Call your function to create the collection here
        st.sidebar.success(f"Collection '{collection_name}' created successfully!")
        st.sidebar.button('Dismiss', key='dismiss')
        pass

    if uploaded_file is not None:
        # Do something with the file
        # This is a placeholder for the implementation
        # file_contents = uploaded_file[0].read()
        pass

    # React to user input
    if prompt := st.chat_input("What's up?"):
        try:
            # Display user message in chat message container
            st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("assistant", avatar=FRIDAY_AVATAR):
                with st.spinner("Thinking!"):
                    logging.info("User input: %s, chat mode: %s, chat with: %s", prompt, chat_mode, 'friday')
                    if use_private_data_toggle:
                        response = ask_friday(prompt, chat_mode, 'friday')
                    else:
                        response = ask_ham(prompt, st.session_state.messages, chat_mode)

                    logging.info("Friday says: %s", response)
                    st.write(response)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)
        except Exception as e:
            st.error(f"An error occurred while calling friday or ham at line {e.__traceback__.tb_lineno}: {str(e)}")
except Exception as e:
    st.error(f"An error occurred during loading of streamlit app: {str(e)}")

