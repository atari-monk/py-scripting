import requests


from abc import ABC, abstractmethod
from typing import Any, Dict


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