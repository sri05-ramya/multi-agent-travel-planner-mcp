import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def get_weather_from_mcp(destination):

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "weather_tool",
                {"destination": destination}
            )

            return result.content[0].text

async def get_hotels_from_mcp(destination):

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "hotel_tool",
                {"destination": destination}
            )
            return result.content[0].text

async def get_activities_from_mcp(destination):

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "activity_tool",
                {"destination": destination}
            )

            return result.content[0].text        
                            
             