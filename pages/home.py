import streamlit as st

st.title("AI English Grammar Checker")

st.write("""
This website helps users detect and correct grammar errors in English sentences using AI and dataset-based methods.
""")

st.subheader("Features")
st.markdown("""
- 🔍 Detect grammar mistakes
- 🤖 AI-based correction (Google Gemini)
- 📊 Dataset-based error detection
- ⚡ Fast and accurate results
""")

st.subheader("How to use")
st.markdown("""
1. Go to **Input page**
2. Enter your sentence
3. Click **Check**
4. View the result
""")

st.subheader("Example")
st.code("He don't know the answer.")

st.subheader("Technologies Used")
st.markdown("""
- Python
- Streamlit
- Google Generative AI
- Pandas
""")

st.success("Ready to try? Go to Input page!")