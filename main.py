from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict
from agents.travel_planner import travel_planner_agent
from agents.weather_agent import weather_agent
from agents.hotel_agent import hotel_agent
from agents.activity_agent import activity_agent
from agents.final_planner import final_planner_agent
from langgraph.graph import StateGraph, START, END
from database import save_trip

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

class TravelState(TypedDict):
    user_request: str
    destination: str
    days: int
    weather: str
    hotels: str
    activities: str
    final_plan: str


def planner_node(state: TravelState):
    return travel_planner_agent(state, llm)
def weather_node(state: TravelState):
    return weather_agent(state)
def hotel_node(state: TravelState):
    return hotel_agent(state, llm)
def activity_node(state: TravelState):
    return activity_agent(state, llm)
def final_planner_node(state: TravelState):
    return final_planner_agent(state, llm)
#creating the nodes
workflow = StateGraph(TravelState)
workflow.add_node("planner", planner_node)
workflow.add_node("weather", weather_node)
workflow.add_node("hotel", hotel_node)
workflow.add_node("activity", activity_node)
workflow.add_node("final_planner", final_planner_node)

#wroflow strts

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "weather")
workflow.add_edge("weather", "hotel")
workflow.add_edge("hotel", "activity")
workflow.add_edge("activity", "final_planner")
workflow.add_edge("final_planner", END)

app = workflow.compile()

if __name__ == "__main__":

    result = app.invoke({
        "user_request": "Plan a 5-day trip to New York"
    })
    save_trip(result)

    print(result["final_plan"])