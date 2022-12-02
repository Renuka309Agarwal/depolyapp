import streamlit as st  # pip install streamlit
import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lt8ter7g.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    width=200


)


contact_form = """
<form action="https://formsubmit.co/agarwalrenuka773@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")