import streamlit as st
from models.model_controller import check_grammar
def load_css():
    with open("giao_dien/input.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()



st.title("English Grammar Checker")

text = st.text_area("Enter your text")

if st.button("Check"):
    with st.spinner("Checking..."):
        result = check_grammar(text)
    
    st.subheader("Result:")
    st.write(result)

