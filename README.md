# Multi-Agent Travel Planner with MCP

This project is a multi-agent travel planning application built with LangGraph, MCP, FastAPI, and PostgreSQL.

The idea is simple: a user gives a travel request, and different agents handle different parts of the trip. The final planner combines everything into one complete travel plan.

## What this project does

The application uses separate agents for:

- understanding the travel request
- checking weather
- finding hotel suggestions
- finding activities
- creating the final day-by-day plan

The weather, hotel, and activity agents use tools through MCP.

The final trip plan is also saved in PostgreSQL so it can be viewed later.

## Project Flow

```text
User Request
   ↓
FastAPI
   ↓
LangGraph
   ↓
Travel Planner Agent
   ↓
Weather Agent → MCP → Weather Tool
   ↓
Hotel Agent → MCP → Hotel Tool
   ↓
Activity Agent → MCP → Activity Tool
   ↓
Final Planner Agent
   ↓
PostgreSQL

Technologies Used:

Python
LangGraph
LangChain
OpenAI
MCP
FastAPI
Uvicorn
PostgreSQL
Psycopg
Requests



