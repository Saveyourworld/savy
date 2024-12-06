import os  
print(os.getcwd())
import base64
import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="Saveyour",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"  # This hides the default Streamlit sidebar
)

BASE_URL = st.secrets.get("BASE_URL")



# --- PAGE SETUP ---
home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏡",
    default=True,
)

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="👨🏻‍💼",
)

project_1_page = st.Page(
    page="views/portfolio.py",
    title="My Portfolio",
    icon="📂",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon="🤖",
)

project_3_page = st.Page(
    page="views/contact.py",
    title="Contact Me",
    icon="📩",
)

terms_of_service = st.Page(
    page="views/terms_of_service.py",
    title="Terms of Service",
    icon="📑",
)

privacy_policy = st.Page(
    page="views/privacy_policy.py",
    title="Privacy Policy",
    icon="🔏",
)





# Dynamically set BASE_URL for local or hosted environments
BASE_URL = st.secrets.get("BASE_URL", "http://localhost:8501")

# CSS to hide Streamlit UI components (Main Menu, Settings, Rerun)
hide_streamlit_ui = """
<style>
/* Hide the Streamlit hamburger menu (Main Menu) */
#MainMenu {
    visibility: hidden;
    display: none;
}

/* Hide the "Rerun" button at the bottom */
footer {
    visibility: hidden;
    display: none;
}

/* Hide the settings menu (gear icon) */
header {
    visibility: hidden;
    display: none;
}
</style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- Sidebar with Updated Dynamic Links ---
sidebar_html = f"""
<style>
    /* Sidebar styling */
    .sidebar-container {{
        position: fixed;
        top: 15%;
        left: 0;
        height: 50;
        width: 40px;
        background-color: transparent;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 5px 0;
        z-index: 1000;
    }}
    .sidebar-item {{
        margin: 15px 0;
        text-align: center;
        position: relative; /* Tooltip container */
    }}
    .sidebar-item img {{
        width: 30px;
        transition: transform 0.3s ease-in-out;
    }}
    .sidebar-item:hover img {{
        transform: scale(1.2);
    }}
    .sidebar-item:hover::after {{
        content: attr(data-title);
        position: absolute;
        left: 50px;
        top: 50%;
        transform: translateY(-50%);
        background-color: #333;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        white-space: nowrap;
        font-size: 12px;
    }}
</style>
<div class="sidebar-container">
    <!-- Home -->
    <div class="sidebar-item" data-title="Home">
        <a href="{BASE_URL}" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946436.png" alt="Home">
        </a>
    </div>
    <!-- About Me -->
    <div class="sidebar-item" data-title="About Me">
        <a href="{BASE_URL}/about_me" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" alt="About Me">
        </a>
    </div>
    <!-- Portfolio -->
    <div class="sidebar-item" data-title="Portfolio">
        <a href="{BASE_URL}/portfolio" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/1087/1087840.png" alt="Portfolio">
        </a>
    </div>
    <!-- Chat Bot -->
    <div class="sidebar-item" data-title="Chat Bot">
        <a href="{BASE_URL}/chatbot" target="_self">
            <img src="https://i.pinimg.com/originals/9a/11/33/9a1133d4af3b637e1c6c8ff251785f27.jpg" alt="Chat Bot">
        </a>
    </div>
    <!-- Contact Me -->
    <div class="sidebar-item" data-title="Contact Me">
        <a href="{BASE_URL}/contact" target="_self">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Contact Me">
        </a>
    </div>   

<div class="sidebar-item" data-title="Terms of Service">
    <a href="{BASE_URL}/terms_of_service" target="_self">
        <img src="https://cdn3.iconfinder.com/data/icons/purchases-and-sales/512/lista.png" alt="Terms of Service">
    </a>
    </div>

<div class="sidebar-item" data-title="Privacy Policy">
    <a href="{BASE_URL}/privacy_policy" target="_self">
        <img src="https://cdn-icons-png.flaticon.com/512/10348/10348855.png" alt="Privacy Policy">
    </a>
</div>
</div>
"""
st.markdown(sidebar_html, unsafe_allow_html=True)

# --- Use Secrets for Deployment ---
st.sidebar.markdown(
    "Made with 💖 by [Saviour](/contact)", unsafe_allow_html=True
)


# --- NAVIGATION SETUP ---
pg = st.navigation(
    pages=[
        home_page,
        about_page,
        project_1_page,
        project_2_page,
        project_3_page,
        terms_of_service,
        privacy_policy,
    ]
)

# --- RUN NAVIGATION ---
pg.run()





