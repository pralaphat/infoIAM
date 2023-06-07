from flask import Flask, request, redirect, session, url_for, render_template
from flask.json import jsonify
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# You need to set your App ID and App Secret in your .env file
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
FACEBOOK_CLIENT_ID = os.getenv("FB_CLIENT_ID")
FACEBOOK_CLIENT_SECRET = os.getenv("FB_CLIENT_SECRET")

# Base URLs for Facebook OAuth
FACEBOOK_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FACEBOOK_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"

# This function redirects the user to the Facebook login page
@app.route("/login")
def login():
    facebook = OAuth2Session(FACEBOOK_CLIENT_ID, redirect_uri=url_for('callback', _external=True))
    authorization_url, _ = facebook.authorization_url(FACEBOOK_AUTHORIZATION_BASE_URL)
    return redirect(authorization_url)

# This is the callback function that Facebook will redirect the user to after they log in
@app.route("/callback")
def callback():
    facebook = OAuth2Session(FACEBOOK_CLIENT_ID, redirect_uri=url_for('callback', _external=True))
    facebook.fetch_token(FACEBOOK_TOKEN_URL, client_secret=FACEBOOK_CLIENT_SECRET,
                         authorization_response=request.url)
    user_info = facebook.get('https://graph.facebook.com/me?fields=id,name,email').json()

    # Save the user_info in the session
    session['user_info'] = user_info
    return redirect(url_for('profile'))

@app.route("/profile")
def profile():
    # Retrieve user_info from the session
    user_info = session.get('user_info')
    if user_info is None:
        # Redirect to login if no user_info found in session
        return redirect(url_for('login'))

    return render_template('profile.html', user_info=user_info)

# Main route just redirects to login
@app.route("/")
def index():
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
