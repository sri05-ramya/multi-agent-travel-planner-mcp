import asyncio
from mcp_client import get_weather_from_mcp


def weather_agent(state):

    trips = state["trips"]

    weather_results = []

    for trip in trips:

        destination = trip["destination"]

        weather = asyncio.run(
            get_weather_from_mcp(destination)
        )

        weather_results.append({
            "destination": destination,
            "weather": weather
        })

    return {
        "weather": weather_results
    }