def final_planner_agent(state, llm):

    trips = state["trips"]
    weather = state["weather"]
    hotels = state["hotels"]
    activities = state["activities"]
    flights = state["flights"]

    response = llm.invoke(
        f"""
        Create a simple multi-city travel plan.

        Trips:
        {trips}

        Weather:
        {weather}

        Hotels:
        {hotels}

        Activities:
        {activities}

        Flights:
        {flights}

        Create a clear day-by-day travel plan for each destination.
        Include the flight information between destinations.
        Follow the number of days specified for each destination.
        Keep it easy to read.
        """
    )

    return {
        "final_plan": response.content
    }