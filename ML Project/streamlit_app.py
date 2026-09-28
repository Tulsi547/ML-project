import os
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Page Config matching Task 4 Frontend branding
st.set_page_config(
    page_title="Vehicle Insurance Fraud Data - Fraud Intelligence Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling to make the embedded component fill the entire page viewport cleanly
st.markdown("""
<style>
    /* Remove default Streamlit top header padding and margins */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    div[data-testid="stAppViewContainer"] {
        background-color: #080c14 !important;
    }
    iframe {
        width: 100% !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Find standalone_frontend.html
current_dir = Path(__file__).resolve().parent
html_candidates = [
    current_dir / "standalone_frontend.html",
    current_dir.parent / "standalone_frontend.html",
]

html_path = None
for candidate in html_candidates:
    if candidate.exists():
        html_path = candidate
        break

if html_path and html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        frontend_html = f.read()
    # Render Task 4 Frontend UI directly inside Streamlit
    components.html(frontend_html, height=1050, scrolling=True)
else:
    st.error("Error: Task 4 Frontend template (standalone_frontend.html) could not be located.")
