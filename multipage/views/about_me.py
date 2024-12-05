import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


    


 #st.markdown("<h1 style='font-size:50px; font-weight:bold;'>Bold Large Heading</h1>", unsafe_allow_html=True)
 #st.markdown("<p style='font-size:15px; font-weight:bold;'>Regular Paragraph</p>", unsafe_allow_html=True)



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




from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# ---- HERO SECTION ----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/im1age.png", width=250)
with col2:
    st.markdown("<h1 style='font-size:60px; font-weight:bold;'>Saviour Raphael</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px; font-weight:bold;'>Senior Software Engineer, Web developer, Business Consultant, Singer and Songwriter.</p>", unsafe_allow_html=True)
    
    if st.button("📩 Contact Me"):
        show_contact_form()
        
# ---- EXPERIENCE AND QUALIFICATIONS ---
st.write("\n")
st.markdown("<h1 style='font-size:35px; font-weight:bold;'>Work Experience</h1>", unsafe_allow_html=True)
html_content = """
<div style="font-size:20px; font-weight:normal;">
↪   Building and Deploying user-friendly websites using HTML, CSS, and JavaScript frameworks, Worked on e-commerce platforms, blogs, and corporate websites.
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)
st.write("\n")

html_content = """
<div style="font-size:20px; font-weight:normal;">
↪   Front-End Development with Sleek Design, intuitive user interfaces with frameworks like React, Vue.js, or Angular; website optimization for speed and performance across different devices and browsers.
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)
st.write("\n")

html_content = """
<div style="font-size:20px; font-weight:normal;">
↪   Back-End Development with server-side logic using Node.js, Python (Django/Flask, streamlit).
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)

        
# ---- SKILLS ---
st.markdown("<h1 style='font-size:35px; font-weight:bold;'>Basic Skills</h1>", unsafe_allow_html=True)

# Create a collapsible section
with st.expander(" 🔄 Click to Expand/Collapse"):
    
    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪   Front-End Proficiency in HTML, CSS, and JavaScript, Knowledge of frameworks like React, Angular, or Vue.js.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("\n")


    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪   Back-End Development familiarity with server-side programming languages like Node.js, PHP, Python, or Ruby; experience with frameworks like Express.js, Django, or Laravel.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("\n")


    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪   Database Management with SQL (MySQL, PostgreSQL) and NoSQL (MongoDB) databases; Ability to optimize database queries and manage data efficiently.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("\n")

    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪   Version Control with platforms like GitHub or GitLab.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("\n")

    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪  Web Design with strong understanding of UI/UX principles and design tools like Figma or Adobe XD.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("\n")

    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪  Website speed optimization, SEO, and cross-browser compatibility.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

st.markdown("<h1 style='font-size:35px; font-weight:bold;'>As Software Developer</h1>", unsafe_allow_html=True)

with st.expander(" 🔄 Click to Expand/Collapse"):
    
    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪        As a software developer, I possess expertise in programming languages, software frameworks, database management, and software design, with additional skills in DevOps tools, microservices, and secure coding practices. I excel in problem-solving, teamwork, and delivering high-quality code with attention to detail.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

######
st.markdown("<h1 style='font-size:35px; font-weight:bold;'>As Business Consultant</h1>", unsafe_allow_html=True)

with st.expander(" 🔄 Click to Expand/Collapse"):
    
    html_content = """
    <div style="font-size:20px; font-weight:normal;">
    ↪      As a business consultant, I specialize in strategic planning, market research, and financial analysis to help organizations align with their goals, identify growth opportunities, and optimize operations. I have expertise in change management, digital transformation, and risk mitigation, ensuring smooth transitions and regulatory compliance. By leveraging industry-specific insights and fostering strong client relationships, I drive sustainable growth and deliver actionable solutions across diverse sectors.
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

####

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("static/de-fotor-20241201153116 (1).png", width=550)
with col2:
    
    st.markdown("<p style='font-size:18px; font-weight:normal;'><em>Hey there, 👋 do you really want to know me on a personal level? Then feel free to reach out 😎</em></p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 1, 1])  # Adjust column ratios for spacing

with col2:  # Center column
    st.image("assets/IMG_20241129_044554_911 (1).jpg", width=160)


with col1:
    st.markdown("<p style='font-size:20px; font-weight:normal;'></p>", unsafe_allow_html=True)




# Spacer to simulate content
st.markdown("<div style='height: 400px;'></div>", unsafe_allow_html=True)

# Footer content
st.markdown("---")  # Horizontal line to separate footer

# Footer Layout
with st.container():
    col1, col2, col3 = st.columns([2, 2, 1])

    # Contact Information with logos
    with col1:
        st.subheader("Contact Information")
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/email.png' width='20' style='vertical-align:middle;' /> Email: [saveyourraphael@gmail.com](mailto:saveyourraphael@gmail.com)", unsafe_allow_html=True)
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/phone.png' width='20' style='vertical-align:middle;' /> Phone: +234 702 6403 051", unsafe_allow_html=True)
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/address.png' width='20' style='vertical-align:middle;' /> Address: Lekki Phase 1, Lagos", unsafe_allow_html=True)




    # Quick Links & Awards with logos
    with col2:
        st.subheader("Quick Links & Recognition")
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/link.png' width='25' style='vertical-align:middle;' /> [About Us](/about_me)", unsafe_allow_html=True)
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/link.png' width='25' style='vertical-align:middle;' /> [Services](/portfolio)", unsafe_allow_html=True)
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/link.png' width='25' style='vertical-align:middle;' /> [Contact Us](/contact)", unsafe_allow_html=True)
        st.write("<img src='https://img.icons8.com/ios-filled/50/1E1E1E/link.png' width='25' style='vertical-align:middle;' /> [Whatsapp](https://wa.me/+2349154131744?text=Hello%20and%20welcome,%20%F0%9F%98%8A%20how%20can%20I%20help%20you?)", unsafe_allow_html=True)
# Privacy Policy and Terms of Service with images/icons
with col1:
    st.markdown(
        """
        <div style="text-align:center;">
        <a href="/privacy_policy" target="_self" style="margin-right: 20px;">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7kzisCK53mYcnyoBavS-ZJy0n3JVytUa-GA&s" alt="Privacy Policy" width="30" style="vertical-align:middle;">
            Privacy Policy
        </a>
        </div>
        """,
        unsafe_allow_html=True,
    )        
        
with col1:
    st.markdown(
        """
        <div style="text-align:center;">
        <a href="/terms_of_service" target="_self" style="margin-left: 20px;">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7zNdGUfPidoC0GoauWMYGUkmqKFtT0rfekA&s" width="30" style="vertical-align:middle;">
            Terms of Service
        </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


    # Social Media Links with logos
    with col3:
        st.subheader("Follow Us")
        st.markdown(
            """
            <a href="https://facebook.com" target="_blank" style="margin-right: 10px;">
                <img src="https://img.icons8.com/ios-filled/50/1E1E1E/facebook.png" alt="Facebook" width="30">
            </a>
            <a href="https://twitter.com" target="_blank" style="margin-right: 10px;">
                <img src="https://img.icons8.com/ios-filled/50/1E1E1E/twitter.png" alt="Twitter" width="30">
            </a>
            <a href="https://linkedin.com" target="_blank" style="margin-right: 10px;">
                <img src="https://img.icons8.com/ios-filled/50/1E1E1E/linkedin.png" alt="LinkedIn" width="30">
            </a>
            """,
            unsafe_allow_html=True,
        )





# Newsletter Subscription with professional button
st.markdown("---")
st.subheader("Subscribe to Our Newsletter")
email = st.text_input("Enter your email", placeholder="e.g., example@domain.com")
if st.button("Subscribe"):
    if email:
        st.success("Thank you for subscribing!")
    else:
        st.error("Please enter a valid email.")




# Copyright Section with styling
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: sky blue;'>
        &copy; 2024 Saveyour Inc. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True,
)


# Retrieve the Tracking ID from the secrets file
ga_tracking_id = st.secrets["general"]["ga_tracking_id"]

# Inject Google Analytics script into the app
st.markdown(
    f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_tracking_id}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{ga_tracking_id}');
    </script>
    """,
    unsafe_allow_html=True
)

