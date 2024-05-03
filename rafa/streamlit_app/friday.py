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
BANNER = os.environ.get("DOCKER_BANNER") if IS_DOCKER else os.environ.get("LOCAL_BANNER")

try:
    # Sidebar content
    img = Image.open(BANNER)
    st.sidebar.image(img, use_column_width=False, width=350, clamp=True)
    st.sidebar.markdown('<h4 style="color: black; font-family: Courier, sans-serif; font-size: 20px; font-weight: thin; text-align: center;">THANK GOD IT\'S FRIDAY 😸 </h4>', unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
    chat_with = st.sidebar.selectbox('Talk to...💬', ['🦹‍♀️  Friday | Private knowledge', '🐒 Ham | General knowledge'], key="chat_with")
    chat_mode = st.sidebar.selectbox('Chat mode...💬', ['qa', 'chat'], key="chat_mode")
    choose_your_space = st.sidebar.selectbox('Choose your slice 🍕', ['Enginnering & Techonology', 'People & Culture', 'Product & Design', 'Sales & Marketing', 'Strategy & Operations', 'Support & Success', 'All'])
    st.sidebar.markdown("Data available for 👇")    
    sidebar_labels = {
        'Enginnering & Techonology': 'Labels for Enginnering & Techonology',
        'Fulfilment | Domain': 'Labels for Fulfilment & Domain',
        'People & Culture': 'Labels for People & Culture',
        'Product & Design': 'Labels for Product & Design',
        'Sales & Marketing': 'Labels for Sales & Marketing',
        'Strategy & Operations': 'Labels for Strategy & Operations',
        'Support & Success': 'Labels for Support & Success',
        'All': 'Labels for All'
    }
    st.sidebar.markdown(sidebar_labels.get(choose_your_space, ""))
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


    def ask_friday(query_text, selected_chat_mode, selected_chat_with):
        response = requests.post(
            f'{INTERMEDIARY_SERVER}/query',
            json={'text': query_text, 'chat_mode': selected_chat_mode, 'talk_to': selected_chat_with}
        )
        logging.info("Chat response content: %s", response.text)
        response_text = response.json()['response'].replace("\\n", "\n")

        return response_text


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else FRIDAY_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What's up?"):
        try:
            # Display user message in chat message container
            st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant", avatar=FRIDAY_AVATAR):
                with st.spinner("Thinking!"):
                    logging.info("User input: %s, chat mode: %s, chat with: %s", prompt, chat_mode, chat_with)
                    response = ask_friday(prompt, chat_mode, chat_with)
                    logging.info("Friday says: %s", response)
                    st.write(response)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)
        except Exception as e:
            st.error(f"An error occurred while calling friday: {str(e)}")
except Exception as e:
    st.error(f"An error occurred during loading of streamlit app: {str(e)}")
