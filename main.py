import requests
import json
from time import sleep
from datetime import date

github_api, wakatime_api = 'https://api.github.com/user', 'https://wakatime.com/api/v1/users/current/summaries'

with open('config.json') as f:
    config = json.load(f)

    if not 'GITHUB_API_KEY' in config or not 'WAKATIME_API_KEY' in config:
        print('Missing API key')
        exit(1)

    while True:

        res = requests.get(wakatime_api, params={
            'api_key': config['WAKATIME_API_KEY'],
            'scope': 'read_logged_time',
            'start': date.today(),
            'end': date.today()
        }).json()

        time = res['cummulative_total']['text']

        requests.patch(github_api, headers={
            'Accept': "application/vnd.github.v3+json",
            'Authorization': f'token {config["GITHUB_API_KEY"]}'
        }, json={
            'bio': f'Today ({date.today()}) coded: {time}'
        })

        # Update bio every 15 minutes
        sleep(900)