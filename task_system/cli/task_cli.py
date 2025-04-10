import questionary
from typing import Optional, List
import requests
import json

API_BASE_URL = "http://localhost:8000"

def prompt_task_creation():
    # Mandatory fields
    task_data = {
        "title": questionary.text("Task title:").ask(),
        "description": questionary.text("Task description:").ask(),
        "requirements": prompt_list("Enter requirements (one per line, empty to finish):"),
        "language": questionary.select(
            "Programming language:",
            choices=["python", "javascript", "java", "c++", "go", "rust", "other"]
        ).ask(),
    }

    # Optional fields
    if questionary.confirm("Would you like to add input specifications?").ask():
        task_data["input"] = {
            "description": questionary.text("Input description:").ask(),
            "examples": prompt_list("Enter input examples (one per line, empty to finish):")
        }

    if questionary.confirm("Would you like to add output specifications?").ask():
        task_data["output"] = {
            "description": questionary.text("Output description:").ask(),
            "examples": prompt_list("Enter output examples (one per line, empty to finish):")
        }

    task_data["difficulty"] = questionary.select(
        "Difficulty level:",
        choices=["easy", "medium", "hard"],
        default="medium"
    ).ask()

    task_data["tags"] = prompt_list("Enter tags (comma separated):", comma_separated=True)

    return task_data

def prompt_list(prompt: str, comma_separated: bool = False) -> List[str]:
    if comma_separated:
        answer = questionary.text(prompt).ask()
        return [item.strip() for item in answer.split(",") if item.strip()]
    else:
        items = []
        while True:
            item = questionary.text(f"{prompt}").ask()
            if not item:
                break
            items.append(item)
        return items

def create_task_via_api(task_data):
    response = requests.post(f"{API_BASE_URL}/tasks/", json=task_data)
    if response.status_code == 200:
        print("Task created successfully!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error creating task: {response.text}")

if __name__ == "__main__":
    print("=== Task Creation Wizard ===")
    task_data = prompt_task_creation()
    create_task_via_api(task_data)
