import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="PredictMyPay",
        page_icon="assets/logo.svg",
        layout="wide",  # ✅ Removes default padding and makes it full-width
        initial_sidebar_state="collapsed"  # Optional: hide sidebar by default
    )
