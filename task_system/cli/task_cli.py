import questionary
from typing import List, Optional, Dict, Any
import requests
import json
from enum import Enum, auto
from abc import ABC, abstractmethod

class Operation(Enum):
    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
    LIST = auto()
    QUIT = auto()

class TaskClientInterface(ABC):
    @abstractmethod
    def create_task(self, task_data: Dict[str, Any]) -> requests.Response:
        pass
    
    @abstractmethod
    def get_task(self, task_id: str) -> requests.Response:
        pass
    
    @abstractmethod
    def update_task(self, task_id: str, task_data: Dict[str, Any]) -> requests.Response:
        pass
    
    @abstractmethod
    def delete_task(self, task_id: str) -> requests.Response:
        pass
    
    @abstractmethod
    def list_tasks(self) -> requests.Response:
        pass

class TaskApiClient(TaskClientInterface):
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def create_task(self, task_data: Dict[str, Any]) -> requests.Response:
        return requests.post(f"{self.base_url}/tasks/", json=task_data)
    
    def get_task(self, task_id: str) -> requests.Response:
        return requests.get(f"{self.base_url}/tasks/{task_id}")
    
    def update_task(self, task_id: str, task_data: Dict[str, Any]) -> requests.Response:
        return requests.put(f"{self.base_url}/tasks/{task_id}", json=task_data)
    
    def delete_task(self, task_id: str) -> requests.Response:
        return requests.delete(f"{self.base_url}/tasks/{task_id}")
    
    def list_tasks(self) -> requests.Response:
        return requests.get(f"{self.base_url}/tasks/")

class ResponseHandler:
    @staticmethod
    def handle(response: requests.Response, 
               success_message: Optional[str] = None, 
               display_json: bool = False) -> None:
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

class InputHandler:
    @staticmethod
    def prompt_list(prompt: str, 
                   comma_separated: bool = False, 
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

class OperationStrategy(ABC):
    def __init__(self, client: TaskClientInterface):
        self.client = client
    
    @abstractmethod
    def execute(self) -> None:
        pass

class CreateTaskOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Create New Task ===")
        task_data = {
            "title": questionary.text("Title:").ask(),
            "description": questionary.text("Description:").ask(),
            "requirements": InputHandler.prompt_list("Requirements (one per line, empty to finish):"),
            "language": questionary.select(
                "Language:",
                choices=["python", "javascript", "java", "c++", "go", "rust", "other"]
            ).ask(),
            "difficulty": questionary.select(
                "Difficulty:",
                choices=["easy", "medium", "hard"],
                default="medium"
            ).ask(),
            "tags": InputHandler.prompt_list("Tags (comma separated):", comma_separated=True)
        }

        if questionary.confirm("Add input specifications?").ask():
            task_data["input"] = {
                "description": questionary.text("Input description:").ask(),
                "examples": InputHandler.prompt_list("Input examples (one per line, empty to finish):")
            }

        if questionary.confirm("Add output specifications?").ask():
            task_data["output"] = {
                "description": questionary.text("Output description:").ask(),
                "examples": InputHandler.prompt_list("Output examples (one per line, empty to finish):")
            }

        response = self.client.create_task(task_data)
        ResponseHandler.handle(response, "Task created successfully!")

class ViewTaskOperation(OperationStrategy):
    def execute(self, task_id: Optional[str] = None) -> None:
        print("\n=== View Task ===")
        if not task_id:
            task_id = questionary.text("Enter task ID:").ask()
        
        response = self.client.get_task(task_id)
        ResponseHandler.handle(response, None, display_json=True)

class UpdateTaskOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Update Task ===")
        task_id = questionary.text("Enter task ID to update:").ask()
        
        response = self.client.get_task(task_id)
        if not response.ok:
            ResponseHandler.handle(response)
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
                updated_task[field] = InputHandler.prompt_list(
                    "Enter new requirements (one per line, empty to finish):",
                    default_items=existing_task.get(field, [])
                )
            elif field == "tags":
                updated_task[field] = InputHandler.prompt_list(
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
                        "examples": InputHandler.prompt_list(
                            f"New {field} examples (one per line, empty to finish):",
                            default_items=existing_task.get(field, {}).get("examples", [])
                        )
                    }
            else:
                updated_task[field] = questionary.text(
                    f"New {field}:",
                    default=str(existing_task.get(field, ""))
                ).ask()
        
        response = self.client.update_task(task_id, updated_task)
        ResponseHandler.handle(response, "Task updated successfully!")

class DeleteTaskOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Delete Task ===")
        task_id = questionary.text("Enter task ID to delete:").ask()
        
        if questionary.confirm(
            f"Are you sure you want to delete task {task_id}?", default=False
        ).ask():
            response = self.client.delete_task(task_id)
            ResponseHandler.handle(response, "Task deleted successfully!")

class ListTasksOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Task List ===")
        response = self.client.list_tasks()

        if response.ok:
            tasks = response.json()
            if not tasks:
                print("No tasks found")
                return

            for i, (task_id, task) in enumerate(tasks.items(), 1):
                print(f"{i}. {task['title']} (ID: {task_id})")
                print(f"   Language: {task.get('language', 'N/A')}")
                print(f"   Difficulty: {task.get('difficulty', 'N/A')}")
                print("-" * 40)

            task_ids = list(tasks.keys())
            choices = [
                questionary.Choice(f"View details of task {i+1}", value=task_ids[i])
                for i in range(len(task_ids))
            ] + [questionary.Choice("Return to main menu", value=None)]

            selected = questionary.select(
                "Select a task to view details or return:",
                choices=choices
            ).ask()

            if selected:
                ViewTaskOperation(self.client).execute(selected)
        else:
            ResponseHandler.handle(response)

class OperationFactory:
    @staticmethod
    def create_operation(operation: Operation, client: TaskClientInterface) -> OperationStrategy:
        operations = {
            Operation.CREATE: CreateTaskOperation(client),
            Operation.READ: ViewTaskOperation(client),
            Operation.UPDATE: UpdateTaskOperation(client),
            Operation.DELETE: DeleteTaskOperation(client),
            Operation.LIST: ListTasksOperation(client)
        }
        return operations.get(operation)

class TaskCLI:
    def __init__(self, client: TaskClientInterface):
        self.client = client
    
    def run(self):
        print("=== Task Management CLI ===")
        while True:
            operation = self._select_operation()
            
            if operation == Operation.QUIT:
                break
            
            strategy = OperationFactory.create_operation(operation, self.client)
            if strategy:
                strategy.execute()
    
    def _select_operation(self) -> Operation:
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

def main():
    client = TaskApiClient()
    cli = TaskCLI(client)
    
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()