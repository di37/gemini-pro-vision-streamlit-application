# Gemini Streamlit Application - Image and Video

This application will allow to upload image or video and user can prompt it one time or multiple times. Accordingly, the response will be given by this application.

Note that the code has been modularized for better readability, easy understanding and maintenance.

## Pre-requisites

1. Docker Desktop and Docker Compose. Also, know the commands of docker compose.
2. Google AI Studio API Key - ai.google.dev
3. Google Cloud Service Account with full access to Vertex AI - Refer to https://github.com/di37/getting-started-with-gemini-api.

## Running the Application

1. Run the command as follows.

```
docker compose up
```

2. Navigate to http://localhost:9010/

Note: Ports can be changed in docker-compose.yaml - external port and Dockerfile - internal port.

Our application is now ready to run in our web browser.

### Image example

Photo for the demo taken from:https://variety.com/wp-content/uploads/2020/01/shutterstock_editorial_10522870cv.jpg

### Video example

<img src="https://github.com/di37/mysql-docker-tutorial/blob/main/screenshots/screenshot_01.png?raw=true" width="1000" height="250">

<img src="https://github.com/di37/mysql-docker-tutorial/blob/main/screenshots/screenshot_01.png?raw=true" width="1000" height="250">

Video for the demo taken from: https://all-free-download.com/free-footage/download/tiny_wild_bird_searching_for_food_in_nature_6892037.html

Feel free to make this application more better. And if you like it, please give it a star.
