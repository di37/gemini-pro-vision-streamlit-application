import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def manage_input_fields():
    st.write("Enter a single or multiple prompts.")

    # Initialize session state variables if they don't exist
    if "input_list" not in st.session_state:
        st.session_state.input_list = [""]

    # Function to add a new input field
    def add_input():
        st.session_state.input_list.append("")

    # Function to remove an input field
    def remove_input(index):
        st.session_state.input_list.pop(index)

    # Display the input fields
    for index, value in enumerate(st.session_state.input_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.session_state.input_list[index] = st.text_input(
                f"Input Prompt: {index+1}", value=value
            )
        with col2:
            st.button(
                "Remove", key=f"remove_{index}", on_click=remove_input, args=(index,)
            )

    # Button to add new input field
    st.button("Add new input", on_click=add_input)

    return st.session_state.input_list
