import asyncio
from mcp_client import get_activities_from_mcp


def activity_agent(state, llm):

    trips = state["trips"]
    weather_results = state["weather"]

    activity_results = []

    for trip in trips:

        destination = trip["destination"]
        days = trip["days"]

        weather = next(
            (
                item["weather"]
                for item in weather_results
                if item["destination"] == destination
            ),
            "Weather unavailable"
        )

        activities = asyncio.run(
            get_activities_from_mcp(destination)
        )

        response = llm.invoke(
            f"""
            The user is planning a {days}-day trip to {destination}.

            Weather:
            {weather}

            Activity search results:
            {activities}

            Suggest suitable activities for this trip.

            If the weather is rainy, prefer indoor activities.
            If the weather is good, include outdoor activities.

            Keep the answer short.
            """
        )

        activity_results.append({
            "destination": destination,
            "days": days,
            "activities": response.content
        })

    return {
        "activities": activity_results
    }