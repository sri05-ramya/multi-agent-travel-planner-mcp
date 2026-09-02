import requests

def get_hotels(destination):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": f"hotels in {destination}",
        "format": "json"
    }

    headers = {
        "User-Agent": "multi-agent-trip-planner"
    }
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )
    data = response.json()
    hotels = [item["display_name"] for item in data[:3]]
    return hotels