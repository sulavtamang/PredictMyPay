import streamlit as st

def set_font():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');

        /* Apply font to all major tags */
        body, h1, h2, h3, h4, h5, h6, p, span, div, button, input, textarea {
            font-family: 'Poppins', sans-serif !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
