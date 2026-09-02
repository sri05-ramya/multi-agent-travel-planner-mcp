def final_planner_agent(state, llm):

    destination = state["destination"]
    days = state["days"]
    weather = state["weather"]
    hotels = state["hotels"]
    activities = state["activities"]

    response = llm.invoke(
        f"""
        Create a simple final travel plan.

        Destination: {destination}
        Number of days: {days}

        Weather:
        {weather}

        Hotels:
        {hotels}

        Activities:
        {activities}

        Create a clear day-by-day travel plan.
        Keep it easy to read.
        """
    )

    return {
        "final_plan": response.content
    }