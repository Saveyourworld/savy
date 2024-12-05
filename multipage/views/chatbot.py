import random
import openai
import time
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import streamlit as st


    


# ---- CUSTOM BACKGROUND ----
page_bg_image = f"""
<style>
/* Apply blur only to the app view container */
[data-testid="stAppViewContainer"]::before {{
content: '';
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-image: url("https://img.freepik.com/free-vector/laptop-with-program-code-isometric-icon-software-development-programming-applications-dark-neon_39422-971.jpg?t=st=1732770641~exp=1732774241~hmac=b1b5cd074bdaa0898a4e293f7a03716d353cd8a35b46b9da8a0f29e1c06d4538&w=740");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
filter: blur(5px);
  z-index: 0; /* Ensure it stays behind content */
pointer-events: none;
}}

/* Transparent Header */
[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0); /* Transparent header */
}}

</style>

<div id="background-blur"></div>
"""

st.markdown(page_bg_image, unsafe_allow_html=True)


from datetime import datetime

# Function to handle response generation
def generate_response():
    responses = [
        "Hello! I'm here to assist you. How can I help today? I'm available 24/7 to answer your questions. Feel free to ask me anything! Check out my latest video on YouTube for more information: [My YouTube Video](https://www.youtube.com/@mindsetbreakfastclub).",
        "Did you know you can explore more on my official site? [Visit Now](https://mynextrends.com).",
        "For tips and tutorials, visit my blog: [Products](https://mynextrends.com/solar).",
        "I can assist you with various tasks. Just let me know what you need help with!",
        "Here's a quick guide for getting started: [Start Here](https://www.startguide.com).",
        "Explore my social media profiles for more updates: [Instagram](https://www.instagram.com/saveyour_official?igsh=bWRlYXZldDdrM2xv), [Facebook](https://www.facebook.com/saviour.raphael.547?mibextid=ZbWKwL).",
        "If you're looking for the latest news, check out this link: [Latest Updates](https://www.latestnews.com).",
        "Need more detailed info? Head over to my knowledge base: [Knowledge Base](https://www.knowledgebase.com).",
        "You can also contact us directly via our support page: [Support Page](https://www.support.com)."
    ]
    return responses

# Function to send rating to webhook
def send_rating_to_webhook(rating):
    webhook_url = st.secrets["webhook_url"]
    payload = {
        "rating": rating,
        "timestamp": datetime.now().isoformat(),
        "user_session": st.session_state.session_id,
    }
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            st.success("Thank you for your feedback! The developer has been notified.")
        else:
            st.error("Failed to send rating to the developer. Please try again later.")
    except Exception as e:
        st.error(f"Error sending rating: {e}")

# Function to handle rating submission
def submit_rating(rating):
    st.session_state.ratings.append(rating)
    send_rating_to_webhook(rating)

# Set title for the app
st.title("Chatbot 🤖")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ratings" not in st.session_state:
    st.session_state.ratings = []
if "input_count" not in st.session_state:
    st.session_state.input_count = 0
if "session_id" not in st.session_state:
    st.session_state.session_id = st.secrets["session_id"]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up? 👋🏻"):
    # Increment input count
    st.session_state.input_count += 1

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Check if it's the second input
    if st.session_state.input_count == 2:
        with st.chat_message("assistant"):
            st.markdown("Rate this website:")
            # Provide a rating box
            rating = st.slider("Rate us (1-5 stars)", 1, 5, key="rating_slider")
            if st.button("Submit Rating"):
                submit_rating(rating)
            st.session_state.messages.append({"role": "assistant", "content": "Rate this website:"})
    else:
        # Provide regular responses
        response = generate_response()
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
