import json

def format_json(data, indent=2, level=0, ensure_ascii=False):
    space = " " * (indent * level)
    if isinstance(data, dict):
        if not data:
            return "{}"
        items = []
        for key, value in data.items():
            formatted_value = format_json(value, indent, level+1, ensure_ascii)
            items.append(f'\n{" " * (indent * (level+1))}"{key}": {formatted_value}')
        return "{" + ",".join(items) + f"\n{space}" + "}"
    elif isinstance(data, list):
        if not data:
            return "[]"
        if len(data) == 1:
            single = format_json(data[0], indent, 0, ensure_ascii)
            return f'[{single}]'
        else:
            items = []
            for item in data:
                formatted_item = format_json(item, indent, level+1, ensure_ascii)
                items.append(f'\n{" " * (indent * (level+1))}{formatted_item}')
            return "[" + ",".join(items) + f"\n{space}" + "]"    
    else:
        return json.dumps(data, ensure_ascii=ensure_ascii)
