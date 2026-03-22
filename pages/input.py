import streamlit as st
from models.model_controller import check_grammar

st.title("English Grammar Checker")

text = st.text_area("Enter your text")

if st.button("Check"):
    with st.spinner("Checking..."):
        result = check_grammar(text)
    
    st.subheader("Result:")
    st.write(result)