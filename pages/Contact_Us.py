import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Please enter Your email:")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Portfolio Contact
{raw_message} \n
{user_email}
"""
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Your message was sent!")
