from task_system.cli.TaskClientInterface import TaskClientInterface


from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    def __init__(self, client: TaskClientInterface):
        self.client = client

    @abstractmethod
    def execute(self) -> None:
        pass