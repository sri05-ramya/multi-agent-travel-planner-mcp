from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from main import app as travel_graph
from database import save_trip, get_trips


app = FastAPI(title="Multi-Agent Travel Planner API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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