import os
from dotenv import load_dotenv
from google import genai
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

df = pd.read_csv("./data/Grammar_Correction.csv")

def check_with_dataset(text):
    for _, row in df.iterrows():
        if text.strip().lower() == row["Ungrammatical Statement"].lower():
            return f"""
❌ Error Type: {row["Error Type"]}
❌ Wrong: {row["Ungrammatical Statement"]}

✔ Correct: {row["Standard English"]}
"""
    return None

def check_grammar(text):
    if not text.strip():
        return "Please enter some text!"

    dataset_result = check_with_dataset(text)
    
    if dataset_result:
        return dataset_result
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
Check grammar and correct this sentence.
Also explain the error type.

Sentence: {text}
"""
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

