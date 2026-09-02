import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
def save_trip(state):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
    """
    INSERT INTO trips (
        user_request,
        destination,
        days,
        weather,
        hotels,
        activities,
        final_plan
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    (
        state["user_request"],
        state["destination"],
        state["days"],
        state["weather"],
        state["hotels"],
        state["activities"],
        state["final_plan"]
    )
)
        conn.commit()
        cursor.close()
        conn.close()
def get_trips():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips")
    trips = cursor.fetchall()
    cursor.close()
    conn.close()
    return trips