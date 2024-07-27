import json
import requests
from tkinter import messagebox
import datetime

def get_schedule(day):
    try:
        response = requests.get('https://raw.githubusercontent.com/XiaPlayz/My-Schedule/main/Schedules.json')
        response.raise_for_status()
        schedule = response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showinfo(title="Offline mode", message=f"Error: {e}\nRedirecting to offline database")
        schedule = {
            "Monday": [
                {"time": "9:00 AM - 12:00 PM", "subject": "IT 212: Fundamentals of Database Systems", "faculty": "Ms. Aubrey A. Lavarez", "room": "CET 102"},
                {"time": "4:00 PM - 6:00 PM", "subject": "IT 213: Platform Technologies", "faculty": "Mr. Leslie Sungkit", "room": "3s 104"},
            ],
            "Tuesday": [
                {"time": "4:00 PM - 7:00 PM", "subject": "IT 211: Introduction to Human Computer Interaction", "faculty": "Cielo Tion", "room": "CET 102"},
                {"time": "1:00 PM - 3:00 PM", "subject": "IT 212: Fundamentals of Database Systems", "faculty": "MELODY ABCEDE", "room": "3s 104"},
            ],
            "Wednesday": [
                {"time": "7:30 AM - 9:30 AM", "subject": "IT 211: Introduction to Human Computer Interaction", "faculty": "MELODY ABCEDE", "room": "3s 104"},
                {"time": "1:00 PM - 3:00 PM", "subject": "IT 214: Object Oriented Programming", "faculty": "Ms. Trisha B. Posadas", "room": "3s 104"},
                {"time": "4:00 PM - 7:00 PM", "subject": "IT 213: Platform Technologies", "faculty": "Mr. Leslie Sungkit", "room": "CET 102"},
            ],
            "Thursday": [
                {"time": "9:00 AM - 12:00 PM", "subject": "IT 212: Fundamentals of Database Systems", "faculty": "Ms. Aubrey A. Lavarez", "room": "CET 102"},
                {"time": "1:00 PM - 4:00 PM", "subject": "IT 213: Platform Technologies", "faculty": "Mr. Leslie Sungkit", "room": "CET 102"},
                {"time": "7:30 AM - 9:00 AM", "subject": "IT 214: Object Oriented Programming", "faculty": "Ms. Trisha B. Posadas", "room": "CET 102"},
            ],
            "Friday": [
                {"time": "9:00 AM - 12:00 PM", "subject": "IT 211: Introduction to Human Computer Interaction", "faculty": "Cielo Tion", "room": "CET 102"},
                {"time": "7:30 AM - 9:00 AM", "subject": "IT 214: Object Oriented Programming", "faculty": "Ms. Trisha B. Posadas", "room": "CET 102"},
            ],
        }

    return schedule.get(day, [])

def display_schedule():
    today = datetime.datetime.today().strftime('%A')
    schedule = get_schedule(today)
    if not schedule:
        messagebox.showinfo(title=today, message="No Classes Today")
    else:
        schedule_details = "\n\n".join(
            [f"Time: {item['time']}\nSubject: {item['subject']}\nFaculty: {item['faculty']}\nRoom: {item['room']}" for item in schedule]
        )
        messagebox.showinfo(title=today, message=schedule_details)

if __name__ == "__main__":
    display_schedule()
