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
    athlete = client.get_athlete() # client.protocol.get('/athletes/your_id')
    athlete_id = athlete.id
    # bo = 'hi'
    # kim = 'yo'
    # c = bo + kim
    stats_m = client.protocol.get('/athletes/' + str(athlete_id) + '/stats')

    stats_mi = {
        'run_distance': m_to_mi(stats_m['recent_run_totals']['distance']),
        'run_count': stats_m['recent_run_totals']['count'],
        'run_distance_ytd': m_to_mi(stats_m['ytd_run_totals']['distance']),
        'run_count_ytd': stats_m['ytd_run_totals']['count'],
        'run_distance_all': m_to_mi(stats_m['all_run_totals']['distance']),
        'run_count_all': stats_m['all_run_totals']['count'],
        'ride_distance': m_to_mi(stats_m['recent_ride_totals']['distance']),
        'ride_count': stats_m['recent_ride_totals']['count'],
        'ride_distance_ytd': m_to_mi(stats_m['ytd_ride_totals']['distance']),
        'ride_count_ytd': stats_m['ytd_ride_totals']['count'],
        'ride_distance_all': m_to_mi(stats_m['all_ride_totals']['distance']),
        'ride_count_all': stats_m['all_ride_totals']['count']
    }
    # raise Exception(stats_mi['run_distance'])

    return render_template('index.html', athlete=athlete, stats=stats_mi, athlete_id=athlete)


def m_to_mi(m):
    return round(m * 0.000621371 ,2)


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
