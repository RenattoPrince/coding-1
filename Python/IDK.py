import tkinter as tk
import time
from datetime import datetime

# Your weekly schedule: (DayName, "HH:MM", Task)
SCHEDULE = [
    ("Friday", "15:30", "Multiplication & Division"),
    ("Friday", "16:30", "Decimals"),
    ("Saturday", "10:30", "BIDMAS"),
    ("Saturday", "14:00", "Rounding & Estimation"),
    ("Saturday", "18:00", "Negative Numbers"),
    ("Sunday", "13:30", "Angle Rules"),
    ("Sunday", "18:00", "Time Calculations"),
    ("Monday", "15:30", "Graphs & Charts"),
    ("Monday", "16:30", "Coordinates"),
    ("Tuesday", "15:30", "Numeracy Problem Solving"),
    ("Tuesday", "16:30", "Mixed Practice (random questions)"),
    ("Wednesday", "07:05", "Quick refresher: angle sums, BIDMAS, rounding")
]

seen_today = set()
current_day = datetime.now().strftime("%A")

def reset_seen_if_new_day():
    global current_day, seen_today
    now_day = datetime.now().strftime("%A")
    if now_day != current_day:
        current_day = now_day
        seen_today = set()

def show_popup(task):
    popup = tk.Toplevel(root)
    popup.title("Revision Reminder")
    popup.attributes("-topmost", True)
    tk.Label(popup, text=f"Time for: {task}", font=("Segoe UI", 16)).pack(padx=24, pady=20)
    tk.Button(popup, text="Got it!", command=popup.destroy).pack(pady=12)

def tick():
    reset_seen_if_new_day()
    now_day = datetime.now().strftime("%A")
    now_time = time.strftime("%H:%M")
    for day, hhmm, task in SCHEDULE:
        key = f"{day}-{hhmm}"
        if day == now_day and hhmm == now_time and key not in seen_today:
            seen_today.add(key)
            show_popup(task)
            break
    # Check again in 10 seconds
    root.after(10000, tick)

# UI root
root = tk.Tk()
root.title("Revision Reminder (Running)")
root.geometry("360x160")
tk.Label(root, text="Revision reminders are active.", font=("Segoe UI", 12)).pack(pady=10)
tk.Label(root, text="Keep this window open to receive pop-ups.", fg="#555").pack()

# Test button: shows a popup immediately
tk.Button(root, text="Test popup now", command=lambda: show_popup("Test: this is a reminder")).pack(pady=12)

# Start the periodic check
root.after(1000, tick)
root.mainloop()