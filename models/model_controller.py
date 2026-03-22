# ================CODE GỐC=============
# import os
# from dotenv import load_dotenv
# from google import genai
# import pandas as pd

# load_dotenv()
# api_key = os.getenv("API_KEY")

# client = genai.Client(api_key=api_key)

# df = pd.read_csv("./data/Grammar_Correction.csv")

# def check_with_dataset(text):
#     for _, row in df.iterrows():
#         if text.strip().lower() == row["Ungrammatical Statement"].lower():
#             return f"""
# ❌ Error Type: {row["Error Type"]}
# ❌ Wrong: {row["Ungrammatical Statement"]}

# ✔ Correct: {row["Standard English"]}
# """
#     return None

# def check_grammar(text):
#     if not text.strip():
#         return "Please enter some text!"

#     dataset_result = check_with_dataset(text)
    
#     if dataset_result:
#         return dataset_result
    
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=f"""
# Check grammar and correct this sentence.
# Also explain the error type.

# Sentence: {text}
# """
#         )
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

#  ------CODE ĐG TEST-----
import os
from dotenv import load_dotenv
from google import genai
import pandas as pd
import streamlit as st

# =========================
# LOAD API
# =========================
load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("./data/Grammar_Correction.csv")

# =========================
# CHECK DATASET
# =========================
def check_with_dataset(text):
    for _, row in df.iterrows():
        if text.strip().lower() == row["Ungrammatical Statement"].lower():
            return f"""
❌ Error Type: {row["Error Type"]}
❌ Wrong: {row["Ungrammatical Statement"]}

✔ Correct: {row["Standard English"]}
"""
    return None

# =========================
# TÁCH EXPLANATION
# =========================
def extract_explanation(text):
    parts = text.split("Explanation:")
    if len(parts) == 2:
        return parts[0], parts[1]
    return text, ""

# =========================
# DỊCH EXPLANATION
# =========================
def translate_explanation(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Translate this to Vietnamese:\n{text}"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# =========================
# CHECK GRAMMAR
# =========================
def check_grammar(text):
    if not text.strip():
        return {"main": "Please enter some text!", "explanation": ""}

    dataset_result = check_with_dataset(text)
    
    if dataset_result:
        return {"main": dataset_result, "explanation": ""}

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
Check grammar and correct this sentence.
Also explain the error type.

Sentence: {text}
"""
        )

        main, explanation = extract_explanation(response.text)

        return {
            "main": main,
            "explanation": explanation
        }

    except Exception as e:
        return {"main": f"Error: {str(e)}", "explanation": ""}

# =========================
# STREAMLIT UI
# =========================
st.title("🔥 Grammar Checker")

user_input = st.text_area("✍ Enter your sentence:")

# Nút check
if st.button("Check", key="check_btn"):
    st.session_state.result = check_grammar(user_input)

# Hiển thị kết quả nếu đã check
if "result" in st.session_state:
    result = st.session_state.result

    # Hiển thị phần chính
    st.write(result["main"])

    # Nếu có explanation → cho nút dịch
    if result["explanation"]:
        if st.button("🇻🇳 Translate Explanation", key="translate_btn"):
            vi = translate_explanation(result["explanation"])
            st.write("### 🇻🇳 Vietnamese Explanation:")
            st.write(vi)