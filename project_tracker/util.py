from datetime import datetime

def get_active(data):
    active_records = [entry for entry in data if not entry.get("end_time") and "start_time" in entry]
    return active_records[-1] if active_records else None

def calculate_minutes(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    delta = end - start
    return delta.seconds // 60

def format_time(minutes):
    return f"{minutes // 60:02}:{minutes % 60:02}"
