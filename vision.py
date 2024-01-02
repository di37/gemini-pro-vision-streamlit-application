# Q&A Chatbot
from utils import *
from ui_files import *

# Headers of the app
initial_headers()

# Handle media upload
media_content, media_type = handle_media_upload()

# Handle JSON file upload for authentication
api_key = handle_credentials(media_type=media_type)

input = st.text_input("Input Prompt: ", key="input")

# Allow multiple prompts
st.subheader("Enter Prompts")
# prompts = st.text_area("Input Prompts (separate prompts with a newline)", height=100)
# prompt_list = [prompt.strip() for prompt in prompts.split("\n") if prompt.strip()]

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
        st.button("Remove", key=f"remove_{index}", on_click=remove_input, args=(index,))

prompts = st.session_state.input_list

# Button to add new input field
st.button("Add new input", on_click=add_input)

submit = st.button(f"Tell me about the {media_type}")

# Configure generation and safety settings
generation_config, safety_settings = configure_generation_and_safety(
    SAFETY_SETTINGS, THRESHOLD_OPTIONS
)

## If ask button is clicked
if submit:
    print(f"Response being generated...")
    st.subheader("The Response as follows...")
    start_time = time.time()

    if media_type == "video":
        final_safety_settings = {}
        for setting in safety_settings:
            final_safety_settings[
                SAFETY_SETTINGS_VIDEO_LABELS[setting["category"]]
            ] = THRESHOLD_OPTIONS_VIDEO_LABELS[setting["threshold"]]
    else:
        final_safety_settings = safety_settings

    response = get_gemini_response(
        input,
        media_content=media_content,
        generation_config=generation_config,
        media_type=media_type,
        safety_settings=final_safety_settings,
        api_key=api_key,
    )
    for chunk in response:
        # print(chunk.text) -> For Debugging
        st.write(chunk.text)

    if os.path.exists("tmp/json_data.json"):
        os.remove("tmp/json_data.json")

    st.write(f"Time taken to generate results: {time.time() - start_time:.2f} seconds.")
