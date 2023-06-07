# infoIAM: Facebook Login Integration with Flask

This project is a simple Flask web application that uses Facebook as a social media identity provider. It allows users to log in using their Facebook credentials, and once logged in, it displays the user's name, email, and profile picture.

## Setup

1. **Clone the repository**
    ```
    git clone https://github.com/pralaphat/infoIAM
    cd infoIAM
    ```

2. **Create and activate a virtual environment (optional but recommended)**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Set up a Facebook App**
    - Go to the [Facebook for Developers](https://developers.facebook.com/) website and create a new app.
    - Follow the instructions to set up your app and obtain a client ID and client secret from Facebook.
    - Configure the app settings, including the valid OAuth redirect URIs, and save the changes.

5. **Set environment variables**
    You need to set environment variables for your Facebook App ID and App Secret. These should be kept secret and not shared publicly.
    ```
    export FB_CLIENT_ID=<your-app-id>
    export FB_CLIENT_SECRET=<your-app-secret>
    ```

## Running the Application

1. **Run the Flask application**
    ```
    flask run
    ```

2. **Open a web browser and navigate to** `http://localhost:5000/`


## Deployment

This app is ready to be deployed on platforms like Heroku, which support Python/Flask. For more information on deploying Flask apps, refer to the Flask documentation and the documentation for your chosen platform.

Please note that you'll need to set up your Facebook App credentials (client ID and client secret) in your deployment environment or hosting platform.


## Note

This is a simple proof of concept and not intended for use in a production environment without further modifications. Notably, it does not handle errors or edge cases and it doesn't persist user data across sessions. For a real-world application, these issues would need to be addressed.

