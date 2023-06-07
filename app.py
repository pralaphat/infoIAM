from flask import Flask, request, render_template
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

FB_CLIENT_ID = os.getenv('FB_CLIENT_ID')
FB_CLIENT_SECRET = os.getenv('FB_CLIENT_SECRET')
REDIRECT_URI = 'https://infoiam.herokuapp.com/callback'

AUTHORIZATION_BASE_URL = 'https://www.facebook.com/dialog/oauth'
TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'

app = Flask(__name__)

@app.route("/")
def index():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, _ = facebook.authorization_url(AUTHORIZATION_BASE_URL)
    return render_template('index.html', authorization_url=authorization_url)

@app.route("/callback")
def callback():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=REDIRECT_URI, state=request.args.get('state'))
    token = facebook.fetch_token(TOKEN_URL, client_secret=FB_CLIENT_SECRET, authorization_response=request.url)
    
    # Fetch user profile information along with email and picture
    user_info = facebook.get('https://graph.facebook.com/me?fields=id,name,email,picture').json()

    # Fetch picture URL
    picture_url = user_info['picture']['data']['url'] if 'picture' in user_info and 'data' in user_info['picture'] and 'url' in user_info['picture']['data'] else None
    user_info['picture_url'] = picture_url

    return render_template('profile.html', user_info=user_info)

if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run(debug=True)
