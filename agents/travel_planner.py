from pydantic import BaseModel


class TripDetails(BaseModel):
    destination: str
    days: int


class MultiTripDetails(BaseModel):
    origin: str
    start_date: str
    trips: list[TripDetails]


def travel_planner_agent(state, llm):

    planner_llm = llm.with_structured_output(MultiTripDetails)

    trip = planner_llm.invoke(
    f"""
    Read the user's travel request.

    User request: {state['user_request']}

    Extract:
    - starting city
    - trip start date in YYYY-MM-DD format
    - every destination
    - number of days for each destination
    """
)

    return {
    "origin": trip.origin,
    "start_date": trip.start_date,
    "trips": [item.model_dump() for item in trip.trips]
}