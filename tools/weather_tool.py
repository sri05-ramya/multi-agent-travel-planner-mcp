import requests


def get_weather(destination):

    url = f"https://wttr.in/{destination}?format=3"

    response = requests.get(url, timeout=10)

    return response.text