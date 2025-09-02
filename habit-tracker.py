import json
from datetime import date

def load_data():
    try:
        with open('daily.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "habits": ["Exercise", "Read", "Drink water"],
            "streaks": {"Exercise": 0, "Read": 0, "Drink water": 0},
            "daily_log": {}     
        }

def save_data(data):
    with open('daily.json', 'w') as f:
        json.dump(data, f)


def log_daily_habits(data):
    today = date.today().isoformat()
    for habit in data["habits"]:
        done = input(f"Have you done {habit} today? (y/n)")

        if done == "y":
            data["streaks"][habit] += 1
            data["daily_log"].setdefault(today, []).append(habit)

def display_streaks(data):
    print("\n--- Current streaks ---")
    for task, streak in data["streaks"].items():
        print(f"Streaks for {task}: {streak} days.")


def add_new_habit(data):
    new_habit = input("Enter the new habit you want to track: ")
    data["habits"].append(new_habit)
    data["streaks"][new_habit] = 0
    print(f"'{new_habit}' has been added to your habits.")


data = load_data()

while True:
    print("\n--- Habit tracker menu ---")
    print("1. Log today's habits")
    print("2. View streaks")
    print("3. Add a new habit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        log_daily_habits(data)
    elif choice == "2":
        display_streaks(data)
    elif choice == "3":
        add_new_habit(data)
    elif choice == "4":
        save_data(data)
        print("Saving and exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
