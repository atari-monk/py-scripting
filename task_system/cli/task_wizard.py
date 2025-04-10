import questionary
from typing import List, Optional
import requests
import json
from enum import Enum, auto

class Operation(Enum):
    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
    LIST = auto()
    QUIT = auto()

API_BASE_URL = "http://localhost:8000"

def main():
    print("=== Task Management CLI ===")
    while True:
        operation = select_operation()
        
        if operation == Operation.CREATE:
            create_task()
        elif operation == Operation.READ:
            view_task()
        elif operation == Operation.UPDATE:
            update_task()
        elif operation == Operation.DELETE:
            delete_task()
        elif operation == Operation.LIST:
            list_tasks()
        elif operation == Operation.QUIT:
            break

def select_operation() -> Operation:
    choice = questionary.select(
        "What would you like to do?",
        choices=[
            questionary.Choice("Create new task", Operation.CREATE),
            questionary.Choice("View task", Operation.READ),
            questionary.Choice("Update task", Operation.UPDATE),
            questionary.Choice("Delete task", Operation.DELETE),
            questionary.Choice("List all tasks", Operation.LIST),
            questionary.Choice("Quit", Operation.QUIT)
        ]
    ).ask()
    return choice

def create_task():
    print("\n=== Create New Task ===")
    task_data = {
        "title": questionary.text("Title:").ask(),
        "description": questionary.text("Description:").ask(),
        "requirements": prompt_list("Requirements (one per line, empty to finish):"),
        "language": questionary.select(
            "Language:",
            choices=["python", "javascript", "java", "c++", "go", "rust", "other"]
        ).ask(),
        "difficulty": questionary.select(
            "Difficulty:",
            choices=["easy", "medium", "hard"],
            default="medium"
        ).ask(),
        "tags": prompt_list("Tags (comma separated):", comma_separated=True)
    }

    if questionary.confirm("Add input specifications?").ask():
        task_data["input"] = {
            "description": questionary.text("Input description:").ask(),
            "examples": prompt_list("Input examples (one per line, empty to finish):")
        }

    if questionary.confirm("Add output specifications?").ask():
        task_data["output"] = {
            "description": questionary.text("Output description:").ask(),
            "examples": prompt_list("Output examples (one per line, empty to finish):")
        }

    response = requests.post(f"{API_BASE_URL}/tasks/", json=task_data)
    handle_response(response, "Task created successfully!")

def view_task(task_id: Optional[str] = None):
    print("\n=== View Task ===")
    if not task_id:
        task_id = questionary.text("Enter task ID:").ask()
    
    response = requests.get(f"{API_BASE_URL}/tasks/{task_id}")
    handle_response(response, None, display_json=True)

def update_task():
    print("\n=== Update Task ===")
    task_id = questionary.text("Enter task ID to update:").ask()
    
    response = requests.get(f"{API_BASE_URL}/tasks/{task_id}")
    if not response.ok:
        handle_response(response)
        return
    
    existing_task = response.json()
    
    updated_task = existing_task.copy()
    
    fields_to_update = questionary.checkbox(
        "Select fields to update:",
        choices=[
            {"name": "Title", "checked": False, "value": "title"},
            {"name": "Description", "checked": False, "value": "description"},
            {"name": "Requirements", "checked": False, "value": "requirements"},
            {"name": "Language", "checked": False, "value": "language"},
            {"name": "Difficulty", "checked": False, "value": "difficulty"},
            {"name": "Tags", "checked": False, "value": "tags"},
            {"name": "Input", "checked": False, "value": "input"},
            {"name": "Output", "checked": False, "value": "output"}
        ]
    ).ask()
    
    for field in fields_to_update:
        if field == "requirements":
            updated_task[field] = prompt_list(
                "Enter new requirements (one per line, empty to finish):",
                default_items=existing_task.get(field, [])
            )
        elif field == "tags":
            updated_task[field] = prompt_list(
                "Enter new tags (comma separated):",
                comma_separated=True,
                default_items=",".join(existing_task.get(field, []))
            )
        elif field in ["input", "output"]:
            if field not in existing_task or not questionary.confirm(
                f"Keep existing {field}?", default=True
            ).ask():
                updated_task[field] = {
                    "description": questionary.text(
                        f"New {field} description:",
                        default=existing_task.get(field, {}).get("description", "")
                    ).ask(),
                    "examples": prompt_list(
                        f"New {field} examples (one per line, empty to finish):",
                        default_items=existing_task.get(field, {}).get("examples", [])
                    )
                }
        else:
            updated_task[field] = questionary.text(
                f"New {field}:",
                default=str(existing_task.get(field, ""))
            ).ask()
    
    response = requests.put(f"{API_BASE_URL}/tasks/{task_id}", json=updated_task)
    handle_response(response, "Task updated successfully!")

def delete_task():
    print("\n=== Delete Task ===")
    task_id = questionary.text("Enter task ID to delete:").ask()
    
    if questionary.confirm(
        f"Are you sure you want to delete task {task_id}?", default=False
    ).ask():
        response = requests.delete(f"{API_BASE_URL}/tasks/{task_id}")
        handle_response(response, "Task deleted successfully!")

def list_tasks():
    print("\n=== Task List ===")
    response = requests.get(f"{API_BASE_URL}/tasks/")
    
    if response.ok:
        tasks = response.json()
        if not tasks:
            print("No tasks found")
            return
            
        choices = [
            (f"{task['id']}: {task['title']} ({task['language']})", task['id'])
            for task in tasks.values()
        ]
        
        selected_id = questionary.select(
            "Select task to view:",
            choices=choices + [("Back", None)]
        ).ask()
        
        if selected_id:
            view_task(selected_id)
    else:
        handle_response(response)

def prompt_list(prompt: str, comma_separated: bool = False, 
               default_items: Optional[List[str]] = None) -> List[str]:
    if default_items is None:
        default_items = []
    
    if comma_separated:
        default_value = ", ".join(default_items)
        answer = questionary.text(
            prompt,
            default=default_value
        ).ask()
        return [item.strip() for item in answer.split(",") if item.strip()]
    else:
        print(prompt)
        items = []
        for i, default_item in enumerate(default_items):
            item = questionary.text(
                f"[{i+1}]",
                default=default_item
            ).ask()
            if item:
                items.append(item)
        
        while True:
            new_item = questionary.text(
                f"[{len(items)+1}] (empty to finish)"
            ).ask()
            if not new_item:
                break
            items.append(new_item)
        return items

def handle_response(response, success_message: Optional[str] = None, 
                   display_json: bool = False):
    if response.ok:
        if success_message:
            print(f"✓ {success_message}")
        if display_json:
            print(json.dumps(response.json(), indent=2))
    else:
        try:
            error_msg = response.json().get("detail", response.text)
        except:
            error_msg = response.text
        print(f"✗ Error {response.status_code}: {error_msg}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")