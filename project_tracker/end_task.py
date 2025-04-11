from datetime import datetime
from project_tracker.util import calculate_minutes, get_active
from shared_library.json.format import format_json
from shared_library.json.load import load_json
from shared_library.json.save import save_json

def update_end_time_for_active_tasks(file_path):
    data = load_json(file_path)
    if data is None:
        return
    
    current_time = datetime.now().strftime("%H:%M")
    record = get_active(data)

    if record:
        record["end_time"] = current_time
        record["actual_minutes"] = calculate_minutes(record["start_time"], record["end_time"])

    json_string = format_json(data)
    save_json(file_path, json_string)
