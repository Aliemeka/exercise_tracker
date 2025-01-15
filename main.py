import csv


daily_plan = [[f"Day {i}" if i < 100 else f"Final Day", "", ""] for i in range(1, 101)]
# Weekly Weigh-In Data
weigh_in_data = [
    ["Week", "Weight", "Change (+/-)"],
    *daily_plan,
]

# Body Measurements Data
body_measurements_data = [
    ["Date", "Chest", "Waist", "Arms", "Thighs"],
    ["Day 30", "", "", "", ""],
    ["Day 60", "", "", "", ""],
    ["Day 90", "", "", "", ""],
]

# Strength Progress Data
strength_progress_data = [
    ["Exercise", "Day 1", "Day 30", "Day 60", "Day 90"],
    ["Push-Ups", "", "", "", ""],
    ["Squats", "", "", "", ""],
    ["Pull-Ups", "", "", "", ""],
    ["Plank", "", "", "", ""],
]


def generate_tracker_file(filename: str, data_list: list) -> None:
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_list)

    print(f"CSV file '{filename}' has been generated.")


generate_tracker("100 Day Progress tracker.csv", weigh_in_data)
generate_tracker("Strength Progress Tracker.csv", strength_progress_data)
generate_tracker("Body measurement sheet.csv", body_measurements_data)
