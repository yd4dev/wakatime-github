import requests
from time import sleep
from datetime import date
import os

github_api, wakatime_api = 'https://api.github.com/user', 'https://wakatime.com/api/v1/users/current/summaries'

while True:

    wakatime = os.environ['WAKATIME_API_KEY']
    github = os.environ['GITHUB_API_KEY']

    res = requests.get(wakatime_api, params={
        'api_key': wakatime,
        'scope': 'read_logged_time',
        'start': date.today(),
        'end': date.today()
    }).json()

    time = res['cumulative_total']['text']
    requests.patch(github_api, headers={
        'Accept': "application/vnd.github.v3+json",
        'Authorization': f'token {github}'
    }, json={
        'bio': f'Today ({date.today()}) coded: {time}'
    })

    # Update bio every 15 minutes
    sleep(900)