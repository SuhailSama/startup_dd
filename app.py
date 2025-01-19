import streamlit as st
import requests

st.title("VC Due Diligence AI")

company = st.text_input("Enter a company name:")
if st.button("Generate Summary"):
    response = requests.get(f"http://127.0.0.1:8000/due_diligence/{company}")
    if response.status_code == 200:
        data = response.json()
        st.subheader("OpenAI Summary")
        st.write(data["openai_summary"])
        st.subheader("Gemini Summary")
        st.write(data["gemini_summary"])
    else:
        st.write("Error fetching data. Try again.")
