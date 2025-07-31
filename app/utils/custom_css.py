
import streamlit as st

def set_custom_css():
    st.markdown("""
        <style>
            /* Set page background to white */
            body, .stApp {
                background-color: #f7f9fc !important;
                color: #000 !important;
            }
                
            /* Remove sidebar if it shows up */
            [data-testid="stSidebar"] {
                display: none;
             }

             /* Make navbar or top elements full-width if needed */
             header, .main {
                width: 100% !important ;
            }
                    
            /* Remove Streamlit's top padding/margin */
            .main .block-container {
                padding-top: 0rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
            }

            /* Reset default margins and paddings */
            html, body {
                margin: 0 !important;
                padding: 0 !important;
                background-color: #f7f9fc !important;
            }

            /* Navbar styles */
            .custom-navbar {
                width: 100vw;
                position: fixed;
                top: 0;
                left: 0;
                z-index: 1000;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #f7f9fc;
                padding: 1rem 2rem;
                box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
            }

            /* Make room for navbar */
            .main {
                margin-top: 80px !important;
                background-color: white;
            }
                
            html, body, .stApp, .main, .block-container {
                margin: 0 !important;
                padding: 0 !important;
                background-color: #f7f9fc !important;
                max-width: 100% !important;
            }

            /* Try to cover any fallback Streamlit container */
            .main .block-container, .block-container {
                padding: 0rem !important;
                margin: 0 auto !important;
                max-width: 100% !important;
            }

            /* Main layout spacing fix */
            .main {
                margin-top: 80px !important;
                padding: 0 !important;
            }
        </style>
    """, unsafe_allow_html=True)
