import requests


def get_activities(destination):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": f"tourist attractions in {destination}",
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

    activities = [
        item["display_name"]
        for item in data[:5]
    ]

    return "\n".join(activities) if activities else "No activities found"