import os
import requests
from dotenv import load_dotenv


load_dotenv()

DUFFEL_ACCESS_TOKEN = os.getenv("DUFFEL_ACCESS_TOKEN")


def get_iata_code(city):

    url = "https://api.duffel.com/places/suggestions"

    headers = {
        "Authorization": f"Bearer {DUFFEL_ACCESS_TOKEN}",
        "Duffel-Version": "v2",
        "Accept": "application/json"
    }

    params = {
        "query": city
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("data"):
        return None

    return data["data"][0]["iata_code"]


def get_flights(origin, destination, departure_date):

    origin_code = get_iata_code(origin)
    destination_code = get_iata_code(destination)

    if not origin_code or not destination_code:
        return {
            "error": "Could not find airport code"
        }

    url = "https://api.duffel.com/air/offer_requests"

    headers = {
        "Authorization": f"Bearer {DUFFEL_ACCESS_TOKEN}",
        "Duffel-Version": "v2",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "data": {
            "slices": [
                {
                    "origin": origin_code,
                    "destination": destination_code,
                    "departure_date": departure_date
                }
            ],
            "passengers": [
                {
                    "type": "adult"
                }
            ],
            "cabin_class": "economy"
        }
    }

    response = requests.post(
        url,
        headers=headers,
        params={
            "return_offers": "true"
        },
        json=data,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    flight_data = result["data"].get("offers", [])

    flights = []

    for item in flight_data[:3]:

        slices = item.get("slices", [])

        if not slices:
            continue

        segments = slices[0].get("segments", [])

        if not segments:
            continue

        first_segment = segments[0]
        last_segment = segments[-1]

        airline = first_segment.get(
            "operating_carrier", {}
        ).get("name", "Unknown airline")

        flight_number = (
            first_segment.get("operating_carrier_flight_number")
            or first_segment.get("marketing_carrier_flight_number")
        )

        flights.append({
            "airline": airline,
            "flight_number": flight_number,
            "from": origin_code,
            "to": destination_code,
            "departure": first_segment.get("departing_at"),
            "arrival": last_segment.get("arriving_at"),
            "stops": len(segments) - 1
        })

    return {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "flights": flights
    }