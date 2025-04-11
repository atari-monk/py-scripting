from typing import Optional
from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.ResponseHandler import ResponseHandler
import questionary


class ViewTaskOperation(OperationStrategy):
    def execute(self, task_id: Optional[str] = None) -> None:
        print("\n=== View Task ===")
        if not task_id:
            task_id = questionary.text("Enter task ID:").ask()

        response = self.client.get_task(task_id)
        ResponseHandler.handle(response, None, display_json=True)