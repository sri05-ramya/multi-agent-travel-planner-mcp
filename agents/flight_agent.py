import asyncio
from datetime import datetime, timedelta
from mcp_client import get_flights_from_mcp


def flight_agent(state):

    origin = state["origin"]
    trips = state["trips"]
    start_date = state["start_date"]

    flight_results = []

    current_date = datetime.strptime(start_date, "%Y-%m-%d")

    first_destination = trips[0]["destination"]

    first_flight = asyncio.run(
        get_flights_from_mcp(
            origin,
            first_destination,
            start_date
        )
    )

    flight_results.append({
        "origin": origin,
        "destination": first_destination,
        "departure_date": start_date,
        "flights": first_flight
    })

    for i in range(len(trips) - 1):

        current_date = current_date + timedelta(
            days=trips[i]["days"]
        )

        departure_date = current_date.strftime("%Y-%m-%d")

        current_city = trips[i]["destination"]
        next_city = trips[i + 1]["destination"]

        flights = asyncio.run(
            get_flights_from_mcp(
                current_city,
                next_city,
                departure_date
            )
        )

        flight_results.append({
            "origin": current_city,
            "destination": next_city,
            "departure_date": departure_date,
            "flights": flights
        })

    return {
        "flights": flight_results
    }