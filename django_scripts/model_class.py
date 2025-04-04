import json
from typing import Dict, Any

def generate_model_code(metadata: Dict[str, Any]) -> str:

    if not metadata or 'model_name' not in metadata or 'fields' not in metadata:
        raise ValueError("Invalid metadata: must contain 'model_name' and 'fields'")

    lines = [
        "from django.db import models",
        "",
        f"class {metadata['model_name']}(models.Model):",
        ""
    ]

    for field in metadata['fields']:
        if not all(k in field for k in ['name', 'type']):
            raise ValueError(f"Invalid field definition: {field}")

        field_type = f"models.{field['type']}"
        params = ", ".join(f"{k}={repr(v)}" for k, v in field.get('params', {}).items())

        field_line = f"    {field['name']} = {field_type}({params})"
        lines.append(field_line)

    if metadata['fields']:
        lines.append("")
        first_field = metadata['fields'][0]['name']
        lines.extend([
            "    def __str__(self):",
            f"        return str(self.{first_field})",
            ""
        ])

    return "\n".join(lines)

def save_model_code(model_code: str, metadata: Dict[str, Any]) -> str:

    if not model_code or not metadata or 'model_name' not in metadata:
        raise ValueError("Invalid model code or metadata")

    filename = f"{metadata['model_name'].lower()}_model.py"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(model_code)
    return filename

def save_model_class():

    try:
        metadata_file = input("📌 Enter path to metadata JSON file: ").strip()

        with open(metadata_file, encoding='utf-8') as f:
            metadata = json.load(f)

        model_code = generate_model_code(metadata)
        print("\nGenerated Model Code:\n")
        print(model_code)

        filename = save_model_code(model_code, metadata)
        print(f"\n✅ Model code saved to {filename}")

    except FileNotFoundError:
        print(f"❌ Error: File not found at {metadata_file}")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON file")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    save_model_class()