import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

def header(url):
    st.markdown(f'<p style="background-color:none;color:blue;font-size:45px;width:100%;align:centre;">{url}</p>',
                unsafe_allow_html=True)
header('TWITTER SENTIMENT ANALYSIS')
# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_bz1uh69q.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    width=400,
)




