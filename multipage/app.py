import streamlit as st
import os

# Import content functions from other Python files
from views.home import display_home
from views.about_me import display_about_me
from views.portfolio import display_portfolio
from views.chatbot import display_chatbot
from views.contact import display_contact
from views.terms_of_service import display_terms
from views.privacy_policy import display_privacy

# Set page configuration
st.set_page_config(
    page_title="Saveyour",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dynamically set BASE_URL based on environment
BASE_URL = st.secrets.get("BASE_URL", "https://saveyour.streamlit.app/")

# Hide Streamlit default UI components
hide_streamlit_ui = """
<style>
#MainMenu, header, footer {
    visibility: hidden;
    display: none;
}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# Sidebar with updated dynamic links
sidebar_html = f"""
<style>
    .sidebar-container {{
        position: fixed;
        top: 15%;
        left: 0;
        width: 40px;
        background-color: transparent;
        z-index: 1000;
    }}
    .sidebar-item {{
        margin: 15px 0;
        text-align: center;
    }}
    .sidebar-item img {{
        width: 30px;
        transition: transform 0.3s ease-in-out;
    }}
    .sidebar-item:hover img {{
        transform: scale(1.2);
    }}
</style>
<div class="sidebar-container">
    <div class="sidebar-item" data-title="Home">
        <a href="{BASE_URL}?page=home" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946436.png" alt="Home">
        </a>
    </div>
    <div class="sidebar-item" data-title="About Me">
        <a href="{BASE_URL}?page=about_me" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" alt="About Me">
        </a>
    </div>
    <div class="sidebar-item" data-title="Portfolio">
        <a href="{BASE_URL}?page=portfolio" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1087/1087840.png" alt="Portfolio">
        </a>
    </div>
    <div class="sidebar-item" data-title="Chat Bot">
        <a href="{BASE_URL}?page=chatbot" target="_self">
            <img src="https://i.pinimg.com/originals/9a/11/33/9a1133d4af3b637e1c6c8ff251785f27.jpg" alt="Chat Bot">
        </a>
    </div>
    <div class="sidebar-item" data-title="Contact Me">
        <a href="{BASE_URL}?page=contact" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Contact Me">
        </a>
    </div>
    <div class="sidebar-item" data-title="Terms of Service">
        <a href="{BASE_URL}?page=terms_of_service" target="_self">
            <img src="https://cdn3.iconfinder.com/data/icons/purchases-and-sales/512/lista.png" alt="Terms of Service">
        </a>
    </div>
    <div class="sidebar-item" data-title="Privacy Policy">
        <a href="{BASE_URL}?page=privacy_policy" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/10348/10348855.png" alt="Privacy Policy">
        </a>
    </div>
</div>
"""
st.markdown(sidebar_html, unsafe_allow_html=True)

# Navigation simulation using query params
page = st.experimental_get_query_params().get("page", ["home"])[0]

# Page routing
if page == "home":
    display_home()

elif page == "about_me":
    display_about_me()

elif page == "portfolio":
    display_portfolio()

elif page == "chatbot":
    display_chatbot()

elif page == "contact":
    display_contact()

elif page == "terms_of_service":
    display_terms()

elif page == "privacy_policy":
    display_privacy()

else:
    st.error("Page not found.")
