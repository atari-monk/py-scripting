from datetime import datetime
from shared_library.json.format import format_json
from shared_library.json.load import load_json
from shared_library.json.save import save_json

def get_new_link_input():
    name = input("Enter link name: ")
    url = input("Enter URL: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    tags = [tag.strip() for tag in tags]
    return name, url, tags

def generate_new_link(name, url, tags):
    current_time = datetime.now().strftime("%Y-%m")
    new_link = {
        "name": name,
        "url": url,
        "tags": tags,
        "created_at": current_time,
    }
    return new_link

def store_new_link(file_path, new_link):
    data = load_json(file_path)
    if data is None:
        return
    data.append(new_link)
    json_string = format_json(data)
    save_json(file_path, json_string)

def store_new_link_by_category(file_path, category, new_link):
    data = load_json(file_path)
    if data is None:
        return    
    if category not in data:
        data[category] = {}
    data[category][new_link['name']] = new_link['url']
    json_string = format_json(data)
    save_json(file_path, json_string)

def add_new_link(file_path_1, file_path_2):
    name, url, tags = get_new_link_input()
    new_link = generate_new_link(name, url, tags)
    category = tags[0] if tags else "uncategorized"
    store_new_link(file_path_1, new_link)
    store_new_link_by_category(file_path_2, category, new_link)
