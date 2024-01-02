import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def configure_generation_and_safety(safety_settings, threshold_options):
    # Add sliders for temperature, top_p, top_k, and max_output_tokens
    st.sidebar.header("Generation Configuration")
    temperature = st.sidebar.slider(
        "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.01
    )
    top_p = st.sidebar.slider(
        "Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.01
    )
    top_k = st.sidebar.slider("Top K", min_value=0, max_value=100, value=40, step=1)
    max_output_tokens = st.sidebar.slider(
        "Max Output Tokens", min_value=1, max_value=4096, value=1024, step=1
    )

    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }

    # Sidebar for safety settings
    st.sidebar.header("Safety Settings")

    # Create a dropdown for each category
    for setting in safety_settings:
        setting["threshold"] = st.sidebar.selectbox(
            f"{setting['category']}",
            threshold_options,
            index=threshold_options.index(setting["threshold"]),
        )

    return generation_config, safety_settings
