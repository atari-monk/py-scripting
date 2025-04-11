from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.ResponseHandler import ResponseHandler


import questionary


class DeleteTaskOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Delete Task ===")
        task_id = questionary.text("Enter task ID to delete:").ask()

        if questionary.confirm(
            f"Are you sure you want to delete task {task_id}?", default=False
        ).ask():
            response = self.client.delete_task(task_id)
            ResponseHandler.handle(response, "Task deleted successfully!")