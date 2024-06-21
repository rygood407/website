import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

Image_3=("C:\Serious Images\imagess2.png")
st.title("About")

with st.container():
    st.write("---")
    st.header("About the Brand")
    st.write("##")
    st.subheader("Fashion has always been my canvas for self-expression and creativity. From a young age, I found myself captivated by the transformative power of clothing and style. Whether flipping through fashion magazines, sketching designs, or experimenting with different looks, I discovered that fashion is more than just fabric and trends—it's a language that speaks volumes about personality and culture.My journey into the world of fashion has been a blend of exploration and education. I've studied the history of fashion icons, delved into the nuances of textile design, and honed my eye for detail. Each piece I wear or create tells a story, reflecting my mood, aspirations, and the world around me.Beyond aesthetics, I'm fascinated by the industry's evolution and its impact on society. I admire designers who push boundaries, challenge norms, and redefine beauty. As I navigate my own style evolution, I seek to inspire others to embrace their individuality and express themselves confidently through fashion. Whether attending fashion shows, curating my wardrobe, or engaging with the global fashion community, I am constantly inspired by the artistry and innovation that surrounds me. My passion for fashion isn't just about what's trendy—it's about celebrating diversity, fostering creativity, and finding beauty in every stitch and silhouette.")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")

with open( "style/style.css" ) as css:
    st.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html= True)
