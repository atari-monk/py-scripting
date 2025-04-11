from task_system.cli.TaskClientInterface import TaskClientInterface


import requests


from typing import Any, Dict


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