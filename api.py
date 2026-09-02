from fastapi import FastAPI
from pydantic import BaseModel

from main import app as travel_graph
from database import save_trip, get_trips


app = FastAPI(title="Multi-Agent Travel Planner API")


class TripRequest(BaseModel):
    user_request: str


@app.post("/plan-trip")
def plan_trip(request: TripRequest):

    result = travel_graph.invoke({
        "user_request": request.user_request
    })

    save_trip(result)

    return {
        "trip_plan": result["final_plan"]
    }

@app.get("/trips")
def read_trips():
    return get_trips()