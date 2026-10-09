import streamlit as st
from dotenv import load_dotenv
from google import genai
import os
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🤖 My AI Assistant")
st.write("Ask Gemini a question!")

prompt = st.text_input("Your question:")

if st.button("Ask Gemini"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                st.write(response.text)

            except Exception:
                st.error("Gemini is temporarily busy. Please try again in a moment.")
    else:
        st.warning("Please enter a question first.")