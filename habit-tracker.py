import json
from datetime import date

habits = ["Exercise", "Read", "Drink water"]
streaks = {"Exercise": 0, "Read": 0, "Drink water": 0}
today = date.today().isoformat()
daily = {}


with open('daily.json', 'r') as file:
    daily = json.load(file)


for habit in habits:
    done = input(f"Have you done {habit} today? (y/n)")

    if done == "y":
        streaks[habit] += 1
        daily.setdefault(today, []).append(habit)

for task, streak in streaks.items():
    print(f"Strike for {task}: {streak} days.")

with open('daily.json', 'w') as f:
    json.dump(daily, f)

print(daily)
