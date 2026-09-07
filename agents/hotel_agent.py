import asyncio
from mcp_client import get_hotels_from_mcp


def hotel_agent(state, llm):

    trips = state["trips"]

    hotel_results = []

    for trip in trips:

        destination = trip["destination"]
        days = trip["days"]

        hotels = asyncio.run(
            get_hotels_from_mcp(destination)
        )

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

        hotel_results.append({
            "destination": destination,
            "days": days,
            "hotels": response.content
        })

    return {
        "hotels": hotel_results
    }