import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import streamlit as st
import os
import google.generativeai as genai
import pathlib
import textwrap
from PIL import Image

import json

from vertexai.preview.generative_models import (
    GenerativeModel,
    Part,
    HarmCategory,
    HarmBlockThreshold,
)
from google.oauth2 import service_account  # importing auth using service_account
import json

import os
import base64

import time
from enum import Enum
from typing import Union, List, Any, Dict


## Function to load OpenAI model and get respones
def get_gemini_response(
    input: Union[str, List[str]],
    media_content: Any,
    generation_config: Dict,
    safety_settings: Union[List[Dict], Dict],
    media_type: str = "image",
    api_key: str = None,
):
    print(f"Safety Settings: {safety_settings}")
    print(f"Generation Config: {generation_config}")  # -> For Debugging
    if media_type == "video":
        print(f"Media type is video.")

        model = GenerativeModel(
            model_name="gemini-pro-vision",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
    else:
        print(f"Media type is image.")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            "gemini-pro-vision",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

    if input != "":
        # For debugging
        # with open("tmp/input.txt", "w") as f:
        #     f.write(str(media_content))
        response = model.generate_content(input + [media_content], stream=True)
    else:
        response = model.generate_content(media_content, stream=True)

    return response
