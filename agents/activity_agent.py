import asyncio
from mcp_client import get_activities_from_mcp


def activity_agent(state, llm):

    destination = state["destination"]
    days = state["days"]
    weather = state["weather"]

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

    return {
        "activities": response.content
    }