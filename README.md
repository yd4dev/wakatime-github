# wakatime-github
Python script that updates your GitHub Bio with your coding time of the day.

## Usage

1. Clone the repo ```git clone https://github.com/Dennis1507/wakatime-github/```
2. Install python and it's **requests** library
3. Create a ```config.json``` file and insert your API keys using the template below:
    - [GitHub Token](https://github.com/settings/tokens)  - Requires ```user``` scope
    - [WakaTime Key](https://wakatime.com/settings/api-key)  - 
4. Start ```py main.py```
        ``` python3 main.py```

config.json Template
```
{
    "WAKATIME_API_KEY": "",
    "GITHUB_API_KEY": ""
}
```
