import streamlit as st
import base64



def render_navbar(current_page='home'):

    # Encode logo
    with open("assets/logo.svg", "rb") as f:
        svg_base64 = base64.b64encode(f.read()).decode()
    
    # Handle page state from query param
    page = st.query_params.get("page", ["home"])[0]
    st.session_state.page = page


    st.markdown(
        f"""
        <style>
            .navbar {{
                margin: 2rem auto 0;
                background-color: ##f7f9fc;
                padding: 1rem 1.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #eee;
                position: sticky;
                top: 0;
                z-index: 999;
                width: 100%;
                flex-wrap: nowrap;
            }}
            .nav-left {{
                color: #FF5F1F;
                font-weight: 700;
                font-size: 1.5rem;
                display: flex;
                align-items: center;
                gap: 8px;
                letter-spacing: 0.5px;
            }}
            
            .nav-right {{
                display: flex;
                align-items: center;
                gap: 25px;
            }}

            @media (max-width: 550px) {{
                .nav-left img {{
                height: 25px !important;
                width: 25px !important;
                }}

                .nav-left span {{
                font-size: 1rem !important;
                }}

                .nav-right{{
                gap: 5px
                }}
            }}
            .nav-link{{
                text-decoration: none !important; /* Force remove underline */
                color: black !important;          /* Reset color */
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: all 0.3s ease-in-out;
                padding: 6px 12px;
                border-radius: 6px;
                display: inline-block;
            }}

            @media (max-width: 550px) {{
                .nav-link{{
                font-size: 0.7rem;
                }}
            }}
            .nav-link:hover {{
                background-color: #f0f0f0;
                color: #008080 !important;
                transform: scale(1.05);
            }}
            .nav-link.active {{
                background-color: #008080;
                color: white !important;
            }}

            @media (max-width: 550px) {{
                .nav-right  
            }}
        </style>

        <div class="navbar">
            <div class="nav-left">
                <img src="data:image/svg+xml;base64,{svg_base64}" alt="logo" style="width:40px; height:40px;" />
                <span style="color:#FF5F1F; font-weight:700; font-size:1.5rem; letter-spacing:0.5px; margin-left:8px; user-select:none;">pMp</span>
            </div>
            <div class="nav-right">
                <a class="nav-link {'active' if current_page == 'home' else ''}" href="?page=home" target="_self">Home</a>
                <a class="nav-link {'active' if current_page == 'predict' else ''}" href="?page=predict" target="_self">Predict</a>
                <a class="nav-link {'active' if current_page == 'about' else ''}" href="?page=about" target="_self">About</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
