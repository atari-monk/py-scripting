import json
import os
from datetime import datetime

CONFIG_FILE = r'C:\atari-monk\code\text-data\date_counters.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"counters": []}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def add_counter(config):
    name = input("\nEnter counter name: ")
    
    start_date_str = input(f"Enter start date for '{name}' (YYYY-MM-DD or 'today'): ")
    if start_date_str.lower() == 'today':
        start_date = datetime.now().date()
    else:
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD or 'today'.")
            return
    
    try:
        interval_days = int(input(f"Enter interval in days for '{name}': "))
        if interval_days <= 0:
            print("Interval must be a positive integer.")
            return
    except ValueError:
        print("Invalid interval. Please enter a positive integer.")
        return
    
    label_1 = input("Enter label for '1' state (e.g., 'Water'): ").strip() or "1"
    label_0 = input("Enter label for '0' state (e.g., 'Don't water'): ").strip() or "0"
    
    initial_value = input(f"Should '{name}' start with {label_1} (1) or {label_0} (0) on {start_date}? (1/0): ")
    if initial_value not in ('0', '1'):
        print(f"Initial value must be either 0 ({label_0}) or 1 ({label_1}).")
        return
    
    active = input(f"Should '{name}' be active? (y/n): ").lower() == 'y'
    
    config["counters"].append({
        "name": name,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "interval_days": interval_days,
        "initial_value": int(initial_value),
        "labels": {
            "1": label_1,
            "0": label_0
        },
        "active": active
    })
    save_config(config)
    status = "active" if active else "inactive"
    print(f"\nCounter '{name}' added successfully ({status})!")
    print(f"Will start with {label_1 if initial_value == '1' else label_0} on {start_date}, alternating every {interval_days} days.")

def calculate_counter_status(counter):
    if not counter.get('active', True):
        return "Off"
    
    start_date = datetime.strptime(counter['start_date'], "%Y-%m-%d").date()
    interval_days = counter['interval_days']
    initial_value = counter['initial_value']
    today = datetime.now().date()
    
    delta = today - start_date
    delta_days = delta.days
    
    if delta_days < 0:
        return None
    
    period = delta_days // interval_days
    return (initial_value + period) % 2

def show_all_counters(config):
    if not config["counters"]:
        print("\nNo counters defined yet.")
        return
    
    print("\nCurrent counter statuses:")
    print("-" * 60)
    for counter in config["counters"]:
        status = calculate_counter_status(counter)
        labels = counter.get("labels", {"1": "1", "0": "0"})
        
        if status == "Off":
            status_str = "Off"
        elif status is None:
            initial_label = labels[str(counter['initial_value'])]
            status_str = f"PENDING (starts with {initial_label} on {counter['start_date']})"
        else:
            status_str = labels[str(status)]
        
        active_status = "Active" if counter.get('active', True) else "Inactive"
        print(f"{counter['name']} ({active_status}): {status_str}")
        print(f"  Start: {counter['start_date']} (initial: {labels[str(counter['initial_value'])]})")
        print(f"  Interval: every {counter['interval_days']} days")
        print(f"  Labels: 1 = {labels['1']}, 0 = {labels['0']}")
        print("-" * 60)

def delete_counter(config):
    if not config["counters"]:
        print("\nNo counters to delete.")
        return
    
    print("\nCurrent counters:")
    for i, counter in enumerate(config["counters"], 1):
        print(f"{i}. {counter['name']} ({'Active' if counter.get('active', True) else 'Inactive'})")
    
    try:
        choice = int(input("\nEnter number of counter to delete (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(config["counters"]):
            deleted = config["counters"].pop(choice - 1)
            save_config(config)
            print(f"\nCounter '{deleted['name']}' deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def toggle_counter(config):
    if not config["counters"]:
        print("\nNo counters to toggle.")
        return
    
    print("\nCurrent counters:")
    for i, counter in enumerate(config["counters"], 1):
        print(f"{i}. {counter['name']} ({'Active' if counter.get('active', True) else 'Inactive'})")
    
    try:
        choice = int(input("\nEnter number of counter to toggle (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(config["counters"]):
            counter = config["counters"][choice - 1]
            current_status = counter.get('active', True)
            counter['active'] = not current_status
            save_config(config)
            new_status = "active" if counter['active'] else "inactive"
            print(f"\nCounter '{counter['name']}' is now {new_status}!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    print("\nMAIN MENU")
    print("1. Add new counter")
    print("2. View all counters")
    print("3. Delete a counter")
    print("4. Toggle counter active status")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    config = load_config()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            add_counter(config)
        elif choice == '2':
            show_all_counters(config)
        elif choice == '3':
            delete_counter(config)
        elif choice == '4':
            toggle_counter(config)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()