import streamlit as st
from utils.page_config import set_page_config
from utils.custom_css import set_custom_css
from utils.font import set_font
from pages.home import home
from pages.predict import predict
from pages.about import about
# from pages.about import about  # Uncomment if about page exists

def main():
    set_page_config()
    set_custom_css()
    set_font()

    # --- Update session state from ?page=... URL parameter ---
    page_param = st.query_params.get("page")

    if page_param:
        st.session_state.page = page_param

    # --- Fallback to default page ---
    elif "page" not in st.session_state:
        st.session_state.page = "home"

    # --- Route based on session state ---
    if st.session_state.page == "home":
        home()
        
    elif st.session_state.page == "predict":
        predict()
    elif st.session_state.page == "about":
        about()
    else:
        st.error("Page not found")

if __name__ == "__main__":
    main()
