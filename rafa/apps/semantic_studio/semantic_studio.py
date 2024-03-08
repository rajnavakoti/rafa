import streamlit as st
from PIL import Image

# Load the image
# image = Image.open('ai_human.jpeg')

# Display the sidebar
st.sidebar.title('Sidebar')

# Display the image and title at the top of the page
# st.image(image, width=700)
st.title('Your App Title')

# Define a list of dictionaries, where each dictionary represents a card
cards = [
    {'Name': 'John Doe', 'Model': 'Model 1', 'Experience': '5 years', 'Current Projects': 'Project 1'},
    {'Name': 'Jane Doe', 'Model': 'Model 2', 'Experience': '3 years', 'Current Projects': 'Project 2'},
    {'Name': 'Jane Doe', 'Model': 'Model 2', 'Experience': '3 years', 'Current Projects': 'Project 2'},
    {'Name': 'Jane Doe', 'Model': 'Model 2', 'Experience': '3 years', 'Current Projects': 'Project 2'},
    {'Name': 'Jane Doe', 'Model': 'Model 2', 'Experience': '3 years', 'Current Projects': 'Project 2'},
    {'Name': 'Jane Doe', 'Model': 'Model 2', 'Experience': '3 years', 'Current Projects': 'Project 2'},
    # Add more cards as needed
]

# Display the cards
for i, card in enumerate(cards):
    if i % 3 == 0:
        st.write('---')  # Add a separator
        st.write('')  # Add empty line for spacing
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(card['Name'])
        st.text('Model: ' + card['Model'])
        st.text('Experience: ' + card['Experience'])
        st.text('Current Projects: ' + card['Current Projects'])
        st.write('---', unsafe_allow_html=True)  # Add a rectangle line border
    with col2:
        st.write('')  # Add empty space for spacing
    with col3:
        st.write('')  # Add empty space for spacing
    if (i + 1) % 3 != 0:
        st.write('')  # Add empty line for spacing
st.write('---')  # Add a separator