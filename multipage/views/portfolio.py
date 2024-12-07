import streamlit as st
import pandas as pd  # pip install pandas
from PIL import Image
import os
import requests
#from streamlit_lottie import st_lottie


    
def display_portfolio():
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

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS -----https://lottie.host/7b01135c-543a-45d3-8851-2510b26f466a/GQg9v7nMr9.json
#lottie_coding = load_lottieurl("https://lottie.host/ede2ffe2-8883-4e5c-bd85-a83664225981/vvMkZVteTV.json")
#img_contact_form = Image.open("fan.webp")
#img_lottie_animation = Image.open("IMG_1715.jpeg")


#left_column, right_column = st.columns(2)
#with right_column:
    #st_lottie(lottie_coding, height=300, key="coding")
st.title(f"My Portfolio", anchor=False)
st.write("##")

if st.button("📩 Contact Me"):
        show_contact_form()




# Image URLs 
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Deco-Glas-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/GE-Appliances-Corporate-Website-Design.png.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://deco-glas.de/en/"  # Replace with your external link for image 1
link2_url = "https://www.geappliances.com/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="DECOGLAS", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="GE APPLIANCES", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Blackster-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/Decor-Systems-Corporate-Website-Design.png.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://www.blackster.com/"  # Replace with your external link for image 1
link2_url = "https://kpmg.com/ng/en/home.html" 

# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="BLACKSTER", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="KPMG", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )


###
# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/PLEX-Corporate-Website-Design.png.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2024/02/bearbike-corporate-website-example-980x513.png.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://www.plex.com/"  # Replace with your external link for image 1
link2_url = "https://www.bikebear.com.my/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="PLEX", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="DARE", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

####
# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Innovify-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/btov-Corporate-Website-Example.jpg.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://innovify.com/"  # Replace with your external link for image 1
link2_url = "https://btov.vc/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="INNOVIFY", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="BTOV", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )
#####

# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/K-1-Packaging-Group-Corporate-Website-Design.png.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/MSoft-Corporate-Website-Design.png.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://k1packaging.com/"  # Replace with your external link for image 1
link2_url = "https://mediasoft.team/en/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="K1", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="MSOFT", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )
###
# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Vision-Board-Media-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Instabase-Corporate-Website-Example.jpg.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://www.linkedin-makeover.com/"  # Replace with your external link for image 1
link2_url = "https://instabase.com/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="VISION", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="INSTABASE", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )


####
# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Actium-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Ashcroft-Law-Firm-Corporate-Website-Example.jpg.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://actiumhealth.com/"  # Replace with your external link for image 1
link2_url = "https://ashcroftlawfirm.com/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="ACTIUM", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="ASHCROFT", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

#####
# Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Instaclustr-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Munro-Corporate-Website-Example.jpg.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://www.instaclustr.com/"  # Replace with your external link for image 1
link2_url = "https://www.munropartners.com.au/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="INSTACLUSTR", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="MUNRO", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    ####
    # Image URLs (replace with your actual image URLs)
image1_url = "https://mycodelesswebsite.com/wp-content/uploads/2022/02/Corint-Media-Corporate-Website-Example.jpg.webp"  # Replace with your image 1 URL
image2_url = "https://mycodelesswebsite.com/wp-content/uploads/2023/12/Clumio-Corporate-Website-Design.png.webp"  # Replace with your image 2 URL

# External link URLs (replace with your actual external link URLs)
link1_url = "https://www.corint-media.com/en/home/"  # Replace with your external link for image 1
link2_url = "https://clumio.com/"
# Desired image width (in pixels)
image_width = 400  # Set the width of the images (adjust to your preference)

# Custom CSS for styling buttons
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: -10px;
    }
    .custom-button {
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .like-button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .like-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .dislike-button {
        background-color: #f44336; /* Red */
        color: white;
    }
    .dislike-button:hover {
        background-color: #da190b;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying two images side by side
col1, col2 = st.columns(2)  # Create two columns

# Image 1 in the first column
with col1:
    st.image(image1_url, caption="COR", use_container_width=False, width=image_width)  # Image 1 with fixed width
    st.write(f"[View Site 👆🏻]({link1_url})", unsafe_allow_html=True)  # Linked text under image 1 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Image 2 in the second column
with col2:
    st.image(image2_url, caption="CLUMIO", use_container_width=False, width=image_width)  # Image 2 with fixed width
    st.write(f"[View Site 👆🏻]({link2_url})", unsafe_allow_html=True)  # Linked text under image 2 (external link)
    st.markdown(
        """
        <div class="button-container">
            <button class="custom-button like-button">👍 Like</button>
            <button class="custom-button dislike-button">👎 Dislike</button>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("##")

# CSS for styling the file uploader section
st.markdown("""
<style>
    .uploader-section {
        padding: 20px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin: 30px 0;
    }
    .uploader-title {
        font-size: 1.8em;
        font-weight: bold;
        color: #FFFFFF; /* WHITE */
        text-align: center;
        margin-bottom: 20px;
    }
    .uploader-description {
        font-size: 1.1em;
        color: #87CEEB;
        text-align: center;
        margin-bottom: 20px;
    }
    .success-message {
        font-size: 1em;
        color: #28a745; /* Green */
        text-align: center;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Ensure an upload folder exists for saving files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Title for the uploader section
st.markdown('<div class="uploader-title">Upload Your Samples</div>', unsafe_allow_html=True)
st.markdown('<div class="uploader-description">Share your files with us! Accepted formats include PDFs, images, and documents. Your samples are safe with us.</div>', unsafe_allow_html=True)

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg", "docx", "txt"])

# Save file to backend if uploaded
if uploaded_file is not None:
    # Save file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display success message
    st.markdown(f'<div class="success-message">✅ Your file "{uploaded_file.name}" has been uploaded successfully!</div>', unsafe_allow_html=True)

# Note to the user
st.markdown('<p style="text-align: center; color: #87CEEB;">Note: Only upload files you have the rights to share.</p>', unsafe_allow_html=True)



# CSS for styling the landscape review section
st.markdown("""
<style>
    .reviews-title {
        font-size: 2em;
        font-weight: bold;
        color: #FFFFFF; /* WHITE */
        text-align: center;
        margin-bottom: 20px;
    }
    .review-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-top: 20px;
    }
    .review {
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 15px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .review-image {
        flex: 0 0 150px;
        height: 100px;
        border-radius: 10px;
        object-fit: cover;
    }
    .review-content {
        flex: 1;
    }
    .review-title {
        font-size: 1.2em;
        font-weight: bold;
        color: #002855; /* Navy Blue */
    }
    .stars {
        color: #FFD700; /* Gold */
        font-size: 1.2em;
        margin: 5px 0;
    }
    .review-text {
        font-size: 1em;
        color: #333;
        margin: 10px 0;
    }
    .author {
        font-style: italic;
        color: #555;
    }
    .model-link {
        color: #002855;
        font-weight: bold;
        text-decoration: none;
    }
    .model-link:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Reviews data
reviews = [
    {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLa-x3rbKTNoD9JW_mbUNMhb7eQAY9Nfxn3w&s",  # Replace with actual image URL
        "title": "Love your Work 👏🏻",
        "stars": "★★★★★",
        "text": "I love the the way you keep to deadlines, the way you treat your clients. There are no better ways to do this.",
        "author": "- Boboli",
        "model": "Makawi",
        "link": "https://clumio.com/"
    },
    {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyQvNh-gFXfuM_022WG3t-Bbd57aPzPCwjYQ&s",  # Replace with actual image URL
        "title": "Excellent features, 🤩 and beautiful!",
        "stars": "★★★★★",
        "text": "The wow factor after seeing it for the 1st time is an understatement. The user interface is the best. You've won my heart 😀",
        "author": "- Tish53",
        "model": "CLUMIO",
        "link": "https://clumio.com/"
    },
    {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJfBXEEvMcJpf5FjY4QCudfnmZEK7bZClGvQ&s",  # Replace with actual image URL
        "title": "Great Developer",
        "stars": "★★★★★",
        "text": "Works great! Looks great! It is very easy to use. My expectations were truly low",
        "author": "- CypWi",
        "model": "ACTIUM",
        "link": "https://actiumhealth.com/"
    }
]
# Title for the review section
st.markdown('<div class="reviews-title">Reviews</div>', unsafe_allow_html=True)

# Render reviews
st.markdown('<div class="review-container">', unsafe_allow_html=True)
for review in reviews:
    st.markdown(f"""
        <div class="review">
            <img src="{review["image"]}" alt="Review Image" class="review-image">
            <div class="review-content">
                <div class="review-title">{review["title"]}</div>
                <div class="stars">{review["stars"]}</div>
                <div class="review-text">{review["text"]}</div>
                <div class="author">{review["author"]}</div>
                <div class="model"><a href="{review["link"]}" class="model-link">Model #: {review["model"]}</a></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


