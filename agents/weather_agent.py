import asyncio
from mcp_client import get_weather_from_mcp


def weather_agent(state):

    destination = state["destination"]

    weather = asyncio.run(get_weather_from_mcp(destination))

    return {
        "weather": weather
    }