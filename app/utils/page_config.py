import streamlit as st
from utils.path_helper import get_asset_path
from utils.image_loader import load_image_base64

def set_page_config():
    icon_path = get_asset_path('logo.svg')
    icon_src = load_image_base64(icon_path)

    st.set_page_config(
        page_title="PredictMyPay",
        page_icon=icon_src,
        layout="wide",  # ✅ Removes default padding and makes it full-width
        initial_sidebar_state="collapsed"  # Optional: hide sidebar by default
    )
