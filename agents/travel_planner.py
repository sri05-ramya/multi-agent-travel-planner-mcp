from pydantic import BaseModel


class TripDetails(BaseModel):
    destination: str
    days: int


def travel_planner_agent(state, llm):

    planner_llm = llm.with_structured_output(TripDetails)

    trip = planner_llm.invoke(
        f"""
        Read the user's travel request.

        User request: {state['user_request']}

        Extract:
        - destination
        - number of days
        """
    )

    return {
        "destination": trip.destination,
        "days": trip.days
    }