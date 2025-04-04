import json
from typing import Dict, Any

def get_field_definition() -> Dict[str, Any]:
    field_name = input("🔹 Field name: ").strip()
    if field_name.lower() == 'done':
        return None

    print("  🔹 Choose field type:")
    print("    1. CharField (Text)")
    print("    2. IntegerField (Number)")
    print("    3. FloatField (Decimal)")
    print("    4. BooleanField (True/False)")
    print("    5. DateTimeField (Date & Time)")
    print("    6. URLField (Web URL)")
    print("    7. TextField (Long text)")
    field_type_choice = input("  🔸 Enter field type number: ").strip()

    field_type_map = {
        "1": "CharField",
        "2": "IntegerField",
        "3": "FloatField",
        "4": "BooleanField",
        "5": "DateTimeField",
        "6": "URLField",
        "7": "TextField"
    }

    field_type = field_type_map.get(field_type_choice, "CharField")
    params = {}

    if field_type == "CharField":
        max_length = input("  ✏️ Enter max length (default 200): ").strip() or "200"
        params["max_length"] = int(max_length)
    
    if field_type == "BooleanField":
        default = input("  ✏️ Set default value (True/False, default False): ").strip().lower()
        if default in ["true", "t", "1"]:
            params["default"] = True
        else:
            params["default"] = False
    
    return {
        "name": field_name,
        "type": field_type,
        "params": params
    }

def generate_model_metadata() -> Dict[str, Any]:
    model_name = input("📌 Enter your model name (e.g., Employee): ").strip()
    app_name = input("📌 Enter your app name (optional, press Enter to skip): ").strip()
    
    print("\n📌 Define your model fields (type 'done' when finished).")
    fields = []
    
    while True:
        field_def = get_field_definition()
        if not field_def:
            break
        fields.append(field_def)
    
    return {
        "model_name": model_name,
        "app_name": app_name if app_name else None,
        "fields": fields
    }

def save_metadata(metadata: Dict[str, Any]) -> str:
    filename = f"{metadata['model_name'].lower()}_model_metadata.json"
    with open(filename, 'w') as f:
        json.dump(metadata, f, indent=2)
    return filename

def save_meta_model():
    metadata = generate_model_metadata()
    filename = save_metadata(metadata)
    print(f"\n✅ Model metadata saved to {filename}")