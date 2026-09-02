from mcp.server.fastmcp import FastMCP
from tools.weather_tool import get_weather
from tools.hotel_tool import get_hotels
from tools.activity_tool import get_activities



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


if __name__ == "__main__":
    mcp.run()
