from task_system.cli.Operation import Operation
from task_system.cli.OperationFactory import OperationFactory
from task_system.cli.TaskClientInterface import TaskClientInterface
import questionary

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