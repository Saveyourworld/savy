import streamlit as st


st.markdown(
    f"""
    <link rel="preload" href="https://github.com/Saveyourworld/savy/blob/Saveyourworld-patch-1/de-fotor-20241201153116%20(1).png?raw=true" as="image">
    <style>   
    .stApp {{
        background-image: url("https://github.com/Saveyourworld/savy/blob/Saveyourworld-patch-1/de-fotor-20241201153116%20(1).png?raw=true");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        background-color: #DEF0F5;
    }}
    @media (max-width: 768px) {{
        .stApp {{
            background-size: 750px 650px; /* Set a fixed width and height */
 /* Adjusts size to fit smaller screens */
            background-position: center; /* Position the background more effectively */
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Add custom CSS for animations and styling
st.markdown(
    f"""
    <style>

    /* Center content in the page */
    .content-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        height: 100vh; /* Full height for vertical centering */
    }}
    
    
    /* Transparent Header */
[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0); /* Transparent header */
}}

/* Reduce the sidebar width */
    [data-testid="stSidebar"] {{
        width: 20px; /* Adjust to your desired width */
        min-width: 20px; /* Prevent sidebar from resizing smaller */
    }}
    
    
    </style>
    """,
    unsafe_allow_html=True,
)


# Add animated typewriter text
st.markdown(
    """
    <div class="typewriter-container">
        <div class="typewriter">Your Journey Starts Here: Explore My Work</div>
        <div class="subtext">Explore. Create. Inspire.</div>
    </div>
    <style>
        /* General Styles */
        .typewriter-container {
            text-align: left; /* Centering the text */
            margin-top: 0px; /* Adding top margin for space */
        }
        /* Typewriter Animation */
        .typewriter {
            font-size: 3.5vw; /* Set text size relative to the viewport width */
            font-weight: bold;
            color: #4c00b0;
            font-family: 'Pacifico', cursive;
            white-space: nowrap;
            overflow: hidden;
            border-right: 4px solid #4c00b0;
            display: grid;
            width: 37ch; /* Match the text length */
            animation: typing 2s steps(20, end), blink 0.6s step-end infinite;
        }
        /* Typing Animation */
        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 20ch;
            }
        }
        /* Blinking Cursor */
        @keyframes blink {
            from, to {
                border-color: transparent;
            }
            50% {
                border-color: #4c00b0;
            }
        }
        /* Subtext below the title */
        .subtext {
            font-size: 2vw; /* Reduce font size proportionally */
            color: #000000;
            margin-top: 0px;
        }

        /* Mobile View Adjustments */
        @media (max-width: 768px) {
            .typewriter {
                font-size: 4vw; /* Larger text for mobile */
                width: 37ch; /* Allow more width on small screens */
            }
            .subtext {
                font-size: 4vw; /* Adjust subtext for mobile */
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# CSS for styling the images, animation, and layout
st.markdown(
    """
    <style>
    /* Container for the welcome message and the images */
    .main-container {
        display: flex;
        align-items: flex-start;
        justify-content: right;
        margin-top: 0px;
        
    }


    /* Cards container */
    .cards-container {
        flex: 2;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
        
    }

    /* Individual card styling */
    .card {
        width: 450px;
        height: 200px;
        border-radius: 10px;
        background-color: #f4f4f4;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.9);
        overflow: hidden;
        transform: translateX(-100%);
        opacity: 0;
        animation: slideIn 2.0s forwards;
        
    }

    /* Animation keyframes */
    @keyframes slideIn {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }

    /* Delays for each card */
    .card:nth-child(1) { animation-delay: 0s; }
    .card:nth-child(2) { animation-delay: 0.3s; }
    .card:nth-child(3) { animation-delay: 0.6s; }
    .card:nth-child(4) { animation-delay: 0.9s; }
    .card:nth-child(5) { animation-delay: 1.2s; }

    /* Caption text styling */
    .caption {
        font-size: 3rem;
        color: #000080;
        margin-top: 0px;
        text-align: center;
        font-family: serif;
        

    }
        
    
    
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML layout for the welcome message and stacked cards
st.markdown(
    """
    <div class="main-container">
        <div>   
        <p>                                                                           </p>
        </div>
        <div class="cards-container">
            <div class="card"><img src="https://www.wordstream.com/wp-content/uploads/2022/07/nonprofit-website-examples-iwmf.png" alt="Template 1" style="width:100%; height:100%;"></div>
            <div class="card"><img src="https://images.ctfassets.net/lh3zuq09vnm2/6v6hASKYhu8sohkJgIUIMW/bd0f0f28e9313f8945fd50474513c08a/03_Freshbooks.jpg" alt="Template 2" style="width:100%; height:100%;"></div>
            <div class="card"><img src="https://www.webdew.com/wp-content/uploads/2024/05/500px-2-1024x612.webp" alt="Template 3" style="width:100%; height:100%;"></div>
            <div class="card"><img src="https://www.hostinger.in/tutorials/wp-content/uploads/sites/2/2023/06/movement-lab-website-homepage.png" alt="Template 4" style="width:100%; height:100%;"></div>
            <div class="card"><img src="https://static.wixstatic.com/media/5e5a34_4ac6b8a5f9b74f8d90dbdcfe2efca15a~mv2.jpg/v1/fill/w_940,h_558,al_c,q_85,enc_auto/5e5a34_4ac6b8a5f9b74f8d90dbdcfe2efca15a~mv2.jpg" alt="Template 5" style="width:100%; height:100%;"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


