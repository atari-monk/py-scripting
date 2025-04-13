import json
from datetime import datetime
import os

base_path = r'C:\atari-monk\code\text-data\project_time'

project_files = [
   fr'{base_path}\py_scripting_time.json'
]

def calculate_total_active_time(day):
    total_active_minutes = 0
    for session in day['sessions']:
        start_time = datetime.strptime(f"{day['date']} {session['start']}", "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(f"{day['date']} {session['end']}", "%Y-%m-%d %H:%M")
        duration = (end_time - start_time).total_seconds() / 60
        total_active_minutes += duration

    return total_active_minutes

def main():
    project_totals = {}

    for file_path in project_files:
        project_name = os.path.basename(file_path).split('_')[0]
        monthly_active_minutes = 0
        yearly_active_minutes = 0

        with open(file_path, 'r') as file:
            data = json.load(file)

        for day in data['days']:
            total_active_minutes = calculate_total_active_time(day)
            monthly_active_minutes += total_active_minutes
            yearly_active_minutes += total_active_minutes

            total_active_hours = total_active_minutes // 60
            remaining_minutes = total_active_minutes % 60
            day['total_active_time'] = {
                "hours": int(total_active_hours),
                "minutes": int(remaining_minutes)
            }

        monthly_active_hours = monthly_active_minutes // 60
        monthly_remaining_minutes = monthly_active_minutes % 60

        yearly_active_hours = yearly_active_minutes // 60
        yearly_remaining_minutes = yearly_active_minutes % 60

        project_totals[project_name] = {
            "monthly_total_active_time": {
                "hours": int(monthly_active_hours),
                "minutes": int(monthly_remaining_minutes)
            },
            "yearly_total_active_time": {
                "hours": int(yearly_active_hours),
                "minutes": int(yearly_remaining_minutes)
            }
        }

        data['monthly_total_active_time'] = project_totals[project_name]['monthly_total_active_time']
        data['yearly_total_active_time'] = project_totals[project_name]['yearly_total_active_time']

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    for project, totals in project_totals.items():
        print(f"Project: {project}")
        print(f"Monthly Total Active Time: {totals['monthly_total_active_time']['hours']} hours and {totals['monthly_total_active_time']['minutes']} minutes")
        print(f"Yearly Total Active Time: {totals['yearly_total_active_time']['hours']} hours and {totals['yearly_total_active_time']['minutes']} minutes")
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()