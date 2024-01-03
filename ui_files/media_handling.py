import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def handle_media_upload():
    uploaded_file = st.file_uploader(
        "**Drag and drop or upload an Image 🖼️ or a Video 📺**",
        type=["jpg", "jpeg", "png", "mp4"],
    )
    media_content = ""
    media_type = "image"

    if uploaded_file is not None:
        if uploaded_file.type.startswith("image/"):
            media_content = Image.open(uploaded_file)
            media_content = media_content.resize((500, 500))
            st.image(media_content, caption="Uploaded Image.", use_column_width=True)

        if uploaded_file.type.startswith("video/"):
            file_bytes = uploaded_file.read()
            data = base64.b64encode(file_bytes)
            media_content = Part.from_data(
                data=base64.b64decode(data), mime_type="video/mp4"
            )
            st.video(uploaded_file)
            media_type = "video"

    return media_content, media_type
