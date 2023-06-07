from flask import Flask, redirect, url_for, request, render_template
from requests_oauthlib import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()

FB_CLIENT_ID = os.getenv("FB_CLIENT_ID")
FB_CLIENT_SECRET = os.getenv("FB_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, _ = facebook.authorization_url("https://www.facebook.com/dialog/oauth")
    return redirect(authorization_url)

@app.route("/callback", methods=["GET"])
def callback():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=REDIRECT_URI)
    facebook.fetch_token(
        "https://graph.facebook.com/v10.0/oauth/access_token",
        client_secret=FB_CLIENT_SECRET,
        authorization_response=request.url,
    )
    user_info = facebook.get("https://graph.facebook.com/me").json()
    return render_template("profile.html", user_info=user_info)

if __name__ == "__main__":
    app.run(debug=True)
