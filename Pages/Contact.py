import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.title("Contact")

with st.container():
    st.write("---")
    st.header("Contact Info")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ryangoodson13.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Details of your problem"></textarea>
        <button type="submit">Send</button>
</form>

"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

with open( "style/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
