import asyncio
from mcp_client import get_hotels_from_mcp


def hotel_agent(state, llm):

    destination = state["destination"]
    hotels = asyncio.run(get_hotels_from_mcp(destination))
    days = state["days"]

    response = llm.invoke(
    f"""
    The user is planning a {days}-day trip to {destination}.

    Hotel search results:
    {hotels}

    Suggest 3 good hotel options or hotel areas for the trip.
    Keep the answer short.
    Do not make up live prices or availability.
    """
)

    return {
        "hotels": response.content
    }