import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *


def handle_credentials(media_type: str = "image"):
    if media_type == "image":
        api_key = st.text_input(
            "🔐 GOOGLE AI STUDIO API KEY - Required For Image.", key="api_key"
        )
        return api_key

    elif media_type == "video":
        uploaded_json = st.file_uploader(
            "🔐 Upload a JSON file which includes Google Service Account Credentials - Required for Video.",
            type=["json"],
        )

        if uploaded_json is not None:
            json_data = json.load(uploaded_json)
            os.makedirs("tmp", exist_ok=True)
            json_path = os.path.join("tmp", "json_data.json")
            with open(json_path, "w") as file:
                json.dump(json_data, file)

            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path
            service_account.Credentials.from_service_account_info(json_data)
            st.success(
                "Environment variable GOOGLE_APPLICATION_CREDENTIALS set from JSON file."
            )
