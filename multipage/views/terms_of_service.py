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



st.title("Terms of Service")
st.markdown("""
### Welcome to Our Terms of Service

These Terms of Service ("Terms") govern your use of our website. By accessing our website, you agree to these terms in full.

---

#### 1. Acceptance of Terms
By accessing or using our services, you agree to comply with these Terms and all applicable laws.

#### 2. Changes to Terms
We reserve the right to modify these Terms at any time. Updates will be posted on this page.

#### 3. Prohibited Conduct
You agree not to:
- Use the website for illegal purposes.
- Disrupt or interfere with the site's operations.

#### 4. Intellectual Property
All content, logos, and designs are owned by us unless stated otherwise.

#### 5. Liability Limitations
We are not liable for any damages resulting from your use of the website.

#### 6. Contact
For questions regarding these Terms, contact us at: [support@saveyour.com](mailto:saveyourrapheal@gmail.com).
""")


# --- Function for Search with Highlight ---
def search_with_highlight(content, search_term):
    if not search_term:
        return content
    highlighted_content = content.replace(
        search_term, f'<span class="highlight">{search_term}</span>'
    )
    return highlighted_content

# Search functionality
search_term = st.text_input("Search Terms of Service", key="terms_search", help="Enter a keyword to search.")
    
    # Terms of Service content
terms_content = """
    1. Introduction: Welcome to Saveyour!
    2. Use of Service: By using this site, you agree to our terms.
    3. User Responsibilities: Please use the platform responsibly.
    4. Disclaimer: Saveyour is not liable for external links or user content.
    """
    # Apply search functionality
highlighted_terms_content = search_with_highlight(terms_content, search_term)
    
    
# FAQs Section
st.subheader("FAQs")
with st.expander("What is the purpose of the Terms of Service?"):
        st.write("The Terms of Service outline the rules and guidelines for using our website.")
with st.expander("Can I share content from this website?"):
        st.write("Yes, but ensure that you give proper credit and follow the rules outlined.")
with st.expander("What happens if I violate the terms?"):
        st.write("Violation of the terms may result in restrictions or suspension of your account.")
    # Display Terms of Service content
st.markdown(highlighted_terms_content, unsafe_allow_html=True)
    