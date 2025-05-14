import streamlit as st
import requests

st.title("Resume Optimizer")

openai_key = st.text_input("OpenAI API Key", type="password")
master_resume = st.text_area("Paste your Master Resume", height=300)
job_description = st.text_area("Paste Job Description", height=300)

if st.button("Optimize Resume"):
    if not openai_key:
        st.warning("You need to enter your OpenAI API key.")
    else:
        with st.spinner("Generating..."):
            response = requests.post("http://127.0.0.1:8000/optimize", json={
                "master_resume": master_resume,
                "job_description": job_description,
                "openai_key": openai_key
            })
            result = response.json()
            st.text_area("Optimized Resume", result['optimized_resume'], height=400)
