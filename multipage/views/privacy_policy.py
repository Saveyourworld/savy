import streamlit as st
import requests



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


st.title("Privacy Policy")
st.markdown("""
### Welcome to Our Privacy Policy

We are committed to protecting your privacy. This policy explains how we collect, use, and share information.

---

#### 1. Information We Collect
We may collect:
- **Personal Information**: Name, email address, phone number, etc.
- **Usage Data**: Pages visited, time spent, and browser type.

#### 2. How We Use Your Information
We use your information to:
- Provide and improve our services.
- Send newsletters (with your consent).

#### 3. Information Sharing
We do not sell your data. We may share it with trusted partners for operational purposes.

#### 4. Data Security
We implement robust security measures to protect your information.

#### 5. Your Rights
You have the right to:
- Access, update, or delete your data.
- Opt out of marketing communications.

#### 6. Cookies
We use cookies to enhance user experience. You can control cookies in your browser settings.

#### 7. Contact
If you have questions about our privacy practices, email us at: [privacy@saveyour.com](mailto:saveyourraphael@gmail.com).
""")



    # FAQs Section
st.subheader("FAQs")
with st.expander("What data do you collect?"):
    st.write("We collect data you provide, such as your name and email, as well as site usage data.")
with st.expander("How is my data protected?"):
    st.write("Your data is stored securely, and we use encryption to ensure it is safe.")
with st.expander("Can I request data deletion?"):
    st.write("Yes, you can contact us at any time to request that we delete your data.")
