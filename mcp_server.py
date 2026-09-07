from mcp.server.fastmcp import FastMCP
from tools.weather_tool import get_weather
from tools.hotel_tool import get_hotels
from tools.activity_tool import get_activities
from tools.flight_tool import get_flights



mcp = FastMCP("travel-tools")


@mcp.tool()
def weather_tool(destination: str) -> str:
    return get_weather(destination)

@mcp.tool()
def hotel_tool(destination: str):
    return get_hotels(destination)

@mcp.tool()
def activity_tool(destination: str):
    return get_activities(destination)

@mcp.tool()
def flight_tool(origin: str, destination: str, departure_date: str):
    return get_flights(origin, destination, departure_date)

if __name__ == "__main__":
    mcp.run()
