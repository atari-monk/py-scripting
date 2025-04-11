import json
from shared_library.json.load import load_json

def print_json(file_path):
    data = load_json(file_path)
    if data is not None:
        print(json.dumps(data, indent=2, ensure_ascii=False, separators=(',', ': ')))
