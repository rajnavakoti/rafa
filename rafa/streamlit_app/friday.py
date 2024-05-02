import streamlit as st
import requests
import json
import os
from PIL import Image

USER_AVATAR = "/app/rafa/assests/user.png"
BOT_AVATAR = "/app/rafa/assests/friday.png"

def query_response(query_text):
    response = requests.post('http://intermediary_server:5001/query', json={'text': query_text})
    print("response content is this:", response.text)
    response_json = json.loads(response.text)
    response_text = response_json['response']
    response_text = response_text.replace("\\n", "\n")
    return response

def chat_response(query_text):
    response = requests.post('http://intermediary_server:5001/query', json={'text': query_text})
    print("chat response content is this:", response.text)
    response_json = json.loads(response.text)
    response_text = response_json['response']
    response_text = response_text.replace("\\n", "\n")
    return response_text

# st.title('Friday')
# image = st.image('path_to_image', use_column_width=False, width=100)
img = Image.open('/app/rafa/assests/tgif.png')
st.sidebar.image(img, use_column_width=False, width=350, clamp=True)
st.sidebar.markdown('<h4 style="color: black; font-family: Courier, sans-serif; font-size: 20px; font-weight: thin; text-align: center;">THANK GOD IT\'S FRIDAY 😸 </h4>',
            unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
st.sidebar.markdown("<br>", unsafe_allow_html=True)  # Add padding  
chat_with = st.sidebar.selectbox('Talk to...💬', ['🦹‍♀️  Friday | Private knowledge', '🐒 Ham | General knowledge'], key="chat_with")
st.sidebar.markdown(f"<h3 style='font-size: 70px;'>{chat_with.title}</h3>", unsafe_allow_html=True)
chat_mode = st.sidebar.selectbox('Chat mode...💬', ['qa', 'chat'], key="chat_mode")
st.sidebar.markdown(f"<h3 style='font-size: 70px;'>{chat_mode.title}</h3>", unsafe_allow_html=True)
choose_your_space = st.sidebar.selectbox('Choose your slice 🍕', ['Enginnering & Techonology', 'People & Culture', 'Product & Design', 'Sales & Marketing', 'Strategy & Operations', 'Support & Success', 'All'])
st.sidebar.markdown("Data available for 👇")    
if choose_your_space == 'Enginnering & Techonology':
    st.sidebar.markdown('Labels for Enginnering & Techonology')
elif choose_your_space == 'Fulfilment | Domain':
    st.sidebar.markdown('Labels for Fulfilment & Domain')
elif choose_your_space == 'People & Culture':
    st.sidebar.markdown('Labels for People & Culture')
elif choose_your_space == 'Product & Design':
    st.sidebar.markdown('Labels for Product & Design')
elif choose_your_space == 'Sales & Marketing':
    st.sidebar.markdown('Labels for Sales & Marketing')
elif choose_your_space == 'Strategy & Operations':
    st.sidebar.markdown('Labels for Strategy & Operations')
elif choose_your_space == 'Support & Success':
    st.sidebar.markdown('Labels for Support & Success')
elif choose_your_space == 'All':
    st.sidebar.markdown('Labels for All')
st.sidebar.markdown("[Documentation](#documentation)")
#st.subheader("I'm an AI assistant 🧠 💬 📚")

title_container = st.container()
col1, col2, col3 = st.columns([1, 5, 20])
image = Image.open('/app/rafa/assests/friday.png')
with title_container:
    with col1:
        st.image(image, width=164, clamp=True, use_column_width=False, output_format='JPEG', channels='RGB', caption=None)
    with col2:
        st.write('&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;')
    with col3:
        st.markdown(' <br/><br/>  <h4 style="color: black; font-family: Courier, sans-serif; font-size: 20px; font-weight: thin;">..not just an AI, I AM FRIDAY</h4>',
            unsafe_allow_html=True)


def ai_response(query_text, selected_chat_mode, selected_chat_with):
    response = requests.post('http://intermediary_server:5001/query', json={'text': query_text, 'chat_mode': selected_chat_mode, 'talk_to': selected_chat_with})
    print("chat response content is this:", response.text)
    response_json = json.loads(response.text)
    response_text = response_json['response']
    response_text = response_text.replace("\\n", "\n")
    return response_text


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What'sup?"):
    # Display user message in chat message container
    st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {query_response(prompt)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("Thinking!"):
            print("user input is: ", prompt)
            print("chat mdoe is: ", chat_mode)
            print("chat with is: ", chat_with)
            response = ai_response(prompt, chat_mode, chat_with)
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)