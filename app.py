import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


def lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

lottie_code4=lottieurl("https://lottie.host/8fe64b37-3aec-4ad3-928f-0298d9aa3700/Bwn9rVWztB.json")
lottie_code1= lottieurl("https://lottie.host/0d980ca7-f8d7-4202-87f5-6b2e7fc7b4cf/zVu5Ksgt4o.json")
lottie_code2= lottieurl("https://lottie.host/48a1e138-336e-439b-ba03-bbc9d65fc4f7/82ghK4lhTI.json")
lottie_code3=lottieurl("https://lottie.host/2b71dcb1-86d8-49e5-adda-b6af8d5d4a70/xvBh4iY5or.json")

Image_3=("C:\Serious Images\imagess2.png")

st.set_page_config(page_title="DIRI", layout="wide",)





with st.container():
    st.title("DIRI")
    st.subheader("Fashion is kinda a joke. I don't get too bogged down in the clothes. For me, it's one big art project, just a canvas to show that fashion should have a brand which has someone behind it who cares about different contexts. Social things. -Virgil Abloh")


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

with st.container():
    st.write("---")
    st.header("About the Brand")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image(Image_3)
    with text_column:
        st.write("Fashion has always been my canvas for self-expression and creativity. From a young age, I found myself captivated by the transformative power of clothing and style. Whether flipping through fashion magazines, sketching designs, or experimenting with different looks, I discovered that fashion is more than just fabric and trends—it's a language that speaks volumes about personality and culture.My journey into the world of fashion has been a blend of exploration and education. I've studied the history of fashion icons, delved into the nuances of textile design, and honed my eye for detail. Each piece I wear or create tells a story, reflecting my mood, aspirations, and the world around me.Beyond aesthetics, I'm fascinated by the industry's evolution and its impact on society. I admire designers who push boundaries, challenge norms, and redefine beauty. As I navigate my own style evolution, I seek to inspire others to embrace their individuality and express themselves confidently through fashion. Whether attending fashion shows, curating my wardrobe, or engaging with the global fashion community, I am constantly inspired by the artistry and innovation that surrounds me. My passion for fashion isn't just about what's trendy—it's about celebrating diversity, fostering creativity, and finding beauty in every stitch and silhouette.")

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







