from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.ResponseHandler import ResponseHandler
from task_system.cli.ViewTaskOperation import ViewTaskOperation


import questionary


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