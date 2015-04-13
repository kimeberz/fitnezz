#!/usr/bin/env python
import os
from flask import Flask, request, render_template, session, redirect, url_for
from stravalib.client import Client

app = Flask(__name__)

# config
app.secret_key = os.environ['SECRET_KEY']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
HOSTNAME = os.environ['HOSTNAME']

@app.route('/')
def index():
    access_token = session.get('access_token')

    if access_token is None:
        return redirect(url_for('login'))

    client = Client(access_token=access_token)
    athlete = client.get_athlete()

    return render_template('index.html', athlete=athlete)


@app.route('/login')
def login():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': HOSTNAME + '/oauth_authorized/'
    }
    client = Client()
    url = client.authorization_url(**params)
    return redirect(url)


@app.route('/oauth_authorized/')
def oauth_authorized():
    client = Client()
    code = request.args.get('code')
    access_token = client.exchange_code_for_token(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        code=code)
    session['access_token'] = access_token
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
