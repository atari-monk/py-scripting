import os
import shutil
from pathlib import Path

def delete_specific_items():

    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent

    items_to_delete = [
        "db.sqlite3",
        "linkshelf",
        "manage.py"
    ]

    for item in items_to_delete:
        item_path = parent_dir / item
        if item_path.exists():
            if item_path.is_file():
                print(f"Deleting file: {item_path}")
                os.remove(item_path)
            elif item_path.is_dir():
                print(f"Deleting directory: {item_path}")
                shutil.rmtree(item_path)
        else:
            print(f"Item not found: {item_path}")

if __name__ == "__main__":
    delete_specific_items()
    print("Deletion complete.")