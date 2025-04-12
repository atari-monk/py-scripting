from datetime import datetime
from shared_library.json.format import format_json
from shared_library.json.load import load_json
from shared_library.json.save import save_json

DATA_FILE = r"C:\atari-monk\code\text-data\sleep.json"

def register_sleep():
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    time_str = input("Enter sleep time (HH:MM, 24-hour format): ").strip()
    
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    
    try:
        datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format. Please try again.")
        return
    
    data = load_json(DATA_FILE)
    data.append({"date": date_str, "time": time_str})
    json_string = format_json(data)
    save_json(DATA_FILE, json_string)
    
    print(f"Sleep recorded: {date_str} at {time_str}")

if __name__ == "__main__":
    register_sleep()
