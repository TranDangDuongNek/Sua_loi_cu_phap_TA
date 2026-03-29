import streamlit as st
def load_css():
    with open("giao_dien/home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

