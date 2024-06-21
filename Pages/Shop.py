import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.title("Shop")

def lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

lottie_code4=lottieurl("https://lottie.host/8fe64b37-3aec-4ad3-928f-0298d9aa3700/Bwn9rVWztB.json")
lottie_code1= lottieurl("https://lottie.host/0d980ca7-f8d7-4202-87f5-6b2e7fc7b4cf/zVu5Ksgt4o.json")
lottie_code2= lottieurl("https://lottie.host/48a1e138-336e-439b-ba03-bbc9d65fc4f7/82ghK4lhTI.json")
lottie_code3=lottieurl("https://lottie.host/2b71dcb1-86d8-49e5-adda-b6af8d5d4a70/xvBh4iY5or.json")

with st.container():
    st.write("---")
    st.header("Shop All")
    left_column, right_column = st.columns((4,4))
    with left_column:
        st.write("##")
        st.header("Shirts")
        st_lottie(lottie_code1, height=180, key=("coding1"))
        st.write("##")
        st.header("Hoodies")
        st_lottie(lottie_code2, height=180, key=("coding2"))

    with right_column:
        st.write("")
        st.write("##")
        st.header("Pants")
        st_lottie(lottie_code3, height=180, key=("coding3"))
        st.write("##")
        st.header("Accessories")
        st_lottie(lottie_code4, height=180, key=("coding4"))

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

with open( "style/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
