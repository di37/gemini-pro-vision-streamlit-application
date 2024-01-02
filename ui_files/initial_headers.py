import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def initial_headers():
    st.set_page_config(page_title="Gemini Image & Video Demo")
    st.header("Gemini Application - Image & Video Demo")

    st.write(
        "This app is to be used to ask questions on image and video that will be uploaded."
    )
