import streamlit as st
st.title("My First AI App")
st.write("Hello! I'm building my first AI application.")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")