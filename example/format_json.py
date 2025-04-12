from shared_library.json.format import format_json

json_data = [
  {},
  {
    "date": "2025-02-28",
    "project": "battleship-ts",
    "task": "Call game API",
    "estimate_minutes": 30,
    "start_time": "12:48",
    "end_time": "13:18",
    "actual_minutes": 30,
    "notes": ["Failed—refactoring broke Vite and Webpack, changes discarded"]
  }
]

print('\nprint json:\n')
print(json_data)
print('\nprint formatted json:\n')
print(format_json(json_data) + '\n')
