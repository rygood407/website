import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="DIRI", layout="wide",)
st.sidebar.success("Select Pages")




with st.container():
    st.title("What is DIRI?")
    st.write("---")
    st.subheader("DIRI is a contemporary fashion brand committed to sustainability and ethical practices in the fashion industry. Founded on the principles of transparency and craftsmanship, DIRI aims to redefine modern luxury by prioritizing quality, longevity, and environmental responsibility. The brand sources eco-friendly materials and partners with artisans who uphold traditional techniques, ensuring each piece is not only stylish but also conscientiously made. DIRI's purpose is to inspire a shift towards a more sustainable fashion future while empowering individuals to express themselves through thoughtfully designed, timeless pieces that make a positive impact on both people and the planet.")




def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

with open( "style/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)







   
      
