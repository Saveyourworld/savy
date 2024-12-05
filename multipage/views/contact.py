import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


    


from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

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

####

# Custom CSS for styling
st.markdown("""
<style>
    .contact-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #FFFFFF; /* Navy Blue */
        text-align: center;
        margin-bottom: 20px;
    }
    .social-icons {
        text-align: center;
        margin: 20px 0;
    }
    .social-icons a {
        text-decoration: none;
        margin: 0 15px;
        color: inherit;
    }
    .social-icons img {
        width: 50px;
        height: 50px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .social-icons img:hover {
        transform: scale(1.1);
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }
    .contact-info {
        font-size: 1.2em;
        text-align: center;
        margin: 20px 0;
        color: #FFFFFF;
    }
    .contact-form {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .map-container {
        margin: 30px 0;
        text-align: center;
    }
    iframe {
        border: none;
        width: 100%;
        height: 300px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

####


# Add the looping typewriter effect
typewriter_html = """
<div class="typewriter-container">
    <div class="typewriter">Don't hesitate to reach out!</div>
</div>
<style>
    .typewriter-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 10vh;
    }

    .typewriter {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        color: #87CEEB; /* SKY BLUEr */
        display: inline-block;
        border-right: 2px solid #5A5A5A; /* Blinking cursor effect */
        white-space: nowrap;
        overflow: hidden;
        width: 0; /* Initially hidden */
        animation: typing 4s steps(30, end) infinite, blink-caret 0.6s step-end infinite;
    }

    @keyframes typing {
        0% {
            width: 0;
        }
        50% {
            width: 100%; /* Fully reveal text */
        }
        100% {
            width: 0; /* Hide text again */
        }
    }

    @keyframes blink-caret {
        from, to {
            border-color: transparent;
        }
        50% {
            border-color: #5A5A5A;
        }
    }
</style>
"""

st.markdown(typewriter_html, unsafe_allow_html=True)


# Social media icons
st.markdown("""
<div class="social-icons">
    <a href="https://www.instagram.com/saveyour_official?igsh=bWRlYXZldDdrM2xv" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" alt="Instagram">
    </a>
    <a href="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.tiktok.com/%40captrends_&ved=2ahUKEwj1-IimqYiKAxX-WEEAHTf3DDkQjjh6BAgfEAE&usg=AOvVaw2ahdVtEJrBBL4TLbsx3-HH" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/3046/3046126.png" alt="TikTok">
    </a>
    <a href="https://www.facebook.com/saviour.raphael.547?mibextid=ZbWKwL" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook">
    </a>
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown("""
<div class="contact-info">
    📧 Email: <a href="mailto:saveyourraphael@gmail.com" style="color: #87CEEB;">saveyourraphael@gmail.com</a><br>
    📞 Phone: <a href="tel:+1234567890" style="color: #87CEEB;">+234 702640 3051</a>
</div>
""", unsafe_allow_html=True)


import re
import streamlit as st
import requests

# Retrieve the webhook URL securely from Streamlit secrets
WEBHOOK_URL = st.secrets.get("WEBHOOK_URL")

# Function to validate email
def is_valid_email(email):    
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

# Function to validate phone number (ensures only digits and exactly 8 to 15 digits)
def is_valid_phone_number(phone):
    # Check if phone number contains only digits and is 8 to 15 digits long
    return phone.isdigit() and 8 <= len(phone) <= 15

def contact_form():
    st.title("Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number (8 to 15 digits)")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        # Initialize error variables
        name_error, email_error, phone_error, message_error = None, None, None, None

        # Validation logic
        if submit_button:
            if not name.strip():
                name_error = "Please provide your name."
            if not email.strip():
                email_error = "Please provide your email address."
            elif not is_valid_email(email.strip()):
                email_error = "Please provide a valid email address."
            if not phone.strip():
                phone_error = "Please provide your phone number."
            elif not is_valid_phone_number(phone.strip()):  # Corrected function name
                phone_error = "Please provide a valid 8-15 digit phone number (digits only)."
            if not message.strip():
                message_error = "Please provide a message."

            # If there are no errors, proceed with the submission
            if not (name_error or email_error or phone_error or message_error):
                if not WEBHOOK_URL:
                    st.error("Email service is not set up. Please try again later.", icon="📧")
                    return

                # Prepare the data payload
                data = {
                    "name": name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                    "message": message.strip(),
                }
                try:
                    # Send the data to the webhook URL
                    response = requests.post(WEBHOOK_URL, json=data)

                    if response.status_code == 200:
                        st.success("Your message has been sent successfully! 🎉", icon="🥳")
                    else:
                        st.error(f"There was an error sending your message (Status Code: {response.status_code}).", icon="😭")
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred while sending your message: {e}", icon="🚨")
            else:
                # Display errors for each invalid field
                if name_error:
                    st.error(name_error, icon="🤝")
                if email_error:
                    st.error(email_error, icon="📩")
                if phone_error:
                    st.error(phone_error, icon="📱")
                if message_error:
                    st.error(message_error, icon="👨‍💻")

# Render the contact form
contact_form()


# Map (Optional)
st.markdown('<div class="contact-title">Find Me Here</div>', unsafe_allow_html=True)
st.markdown("""
<div class="map-container">
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.835434509788!2d-122.41941518468232!3d37.774929279758024!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808581de068f3827%3A0xf4e866d5f3a9307c!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1633645793138!5m2!1sen!2sus" 
        allowfullscreen="" 
        loading="lazy">
    </iframe>
</div>
""", unsafe_allow_html=True)



###

def contact_page():
    st.title("")
    # WhatsApp Number and Pre-filled Message
    whatsapp_number = "+2349154131744"  # Replace with your WhatsApp number
    message = "Hello and welcome, 😊 how can I help you?"  # Optional pre-filled message

    # HTML and CSS for the WhatsApp button (with shaking effect and lively color)
    whatsapp_html = f"""
    <a href="https://wa.me/{whatsapp_number}?text={message}" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
             alt="Chat with us on WhatsApp" 
             style="
                position: fixed; 
                bottom: 20px; 
                right: 20px; 
                width: 60px; 
                height: 60px; 
                z-index: 1000;
                animation: shake 0.5s ease-in-out infinite;
                background-color: #25D366;  /* Lively WhatsApp green */
                border-radius: 50%;
                padding: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
             ">
    </a>
    <style>
        @keyframes shake {{
            0% {{ transform: translateX(0); }}
            25% {{ transform: translateX(-10px); }}
            50% {{ transform: translateX(0); }}
            75% {{ transform: translateX(10px); }}
            100% {{ transform: translateX(0); }}
        }}
    </style>
    """

    # Display the WhatsApp floater with the shake effect and lively green color
    st.markdown(whatsapp_html, unsafe_allow_html=True)

# Display the contact page with the WhatsApp floater
contact_page()


import streamlit as st
import requests

# Add "Join My Team" section
st.header("Join My Team")

# Add a description and animation
st.markdown("""
Are you a passionate developer looking to join a dynamic team?  
We’re seeking talented individuals to collaborate and create amazing projects together!  

Fill out the form below to let us know about you.
""")

# Display an animated collaboration image
st.image(
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", 
    caption="Collaborate and innovate with us!", 
    use_container_width=True
)

# Retrieve the webhook URL from Streamlit secrets
webhook_url = st.secrets["WEBHOOK_URL"]

# Create a styled form for team applications
with st.form("join_team_form"):
    st.subheader("Team Application Form")
    
    # Capture basic details
    name = st.text_input("Full Name *", placeholder="Enter your full name")
    email = st.text_input("Email Address *", placeholder="Enter your email")
    phone = st.text_input("Phone Number", placeholder="Enter your phone number")
    
    # Developer-specific questions
    role = st.selectbox(
        "What role are you applying for? *", 
        ["Frontend Developer", "Backend Developer", "Fullstack Developer", "UI/UX Designer", "Other"]
    )
    skills = st.text_area(
        "List your key skills and technologies you’re proficient in *", 
        placeholder="e.g., Python, React, Node.js, Figma"
    )
    experience = st.slider("Years of Experience *", 0, 20, 1)
    
    # Resume upload
    resume = st.file_uploader("Upload Your Resume (PDF only)", type=["pdf"])
    
    # Motivation or message
    message = st.text_area(
        "Why do you want to join our team? *", 
        placeholder="Tell us why you’d be a great fit!"
    )
    
    # Submit button
    submit_button = st.form_submit_button("Submit Application")
    
    if submit_button:
        if not name or not email or not role or not skills:
            st.error("Please fill out all required fields marked with *.")
        else:
            # Prepare data to send to webhook
            payload = {
                "name": name,
                "email": email,
                "phone": phone,
                "role": role,
                "skills": skills,
                "experience": experience,
                "message": message,
            }
            
            # Send data to webhook
            try:
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 200:
                    st.success(f"Thank you, {name}! Your application has been submitted successfully.")
                else:
                    st.error(f"Failed to submit the application. Please try again. (Error: {response.status_code})")
            except Exception as e:
                st.error(f"An error occurred while submitting the application: {e}")
