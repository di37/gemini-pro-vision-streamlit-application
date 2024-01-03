# Q&A Chatbot
from utils import *
from ui_files import *

# Headers of the app
initial_headers()

# Handle media upload
media_content, media_type = handle_media_upload()

# Handle JSON file upload for authentication
api_key = handle_credentials(media_type=media_type)

# Handle input fields
prompts = manage_input_fields()

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
        prompts,
        media_content=media_content,
        generation_config=generation_config,
        media_type=media_type,
        safety_settings=final_safety_settings,
        api_key=api_key,
    )
    for chunk in response:
        print(chunk.text)  # For Debugging
        st.write(chunk.text)

    if os.path.exists("tmp/json_data.json"):
        os.remove("tmp/json_data.json")

    st.write(f"Time taken to generate results: {time.time() - start_time:.2f} seconds.")
