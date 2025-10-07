import csv
from datetime import datetime

def log_sleep():
    print("🛌 Sleep Tracker")
    
    # Get user input
    bedtime = input("Enter your bedtime (e.g. 23:00): ")
    wake_time = input("Enter your wake time (e.g. 07:50): ")
    mood = input("How do you feel this morning? (e.g. Refreshed, Tired, Groggy): ")

    # Convert times to datetime objects
    try:
        bedtime_dt = datetime.strptime(bedtime, "%H:%M")
        wake_dt = datetime.strptime(wake_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Use HH:MM.")
        return

    # Calculate sleep duration
    if wake_dt < bedtime_dt:
        wake_dt = wake_dt.replace(day=2)  # assumes sleep crosses midnight
    duration = wake_dt - bedtime_dt
    hours = duration.total_seconds() / 3600

    # Save to CSV
    with open("sleep_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().date(), bedtime, wake_time, round(hours, 2), mood])

    print(f"✅ Logged: {round(hours, 2)} hours of sleep. Mood: {mood}")

log_sleep()