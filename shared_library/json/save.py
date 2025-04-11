def save_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)        
    except Exception as e:
        print(f"Error saving JSON: {e}")
