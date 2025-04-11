from task_system.cli.InputHandler import InputHandler
from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.ResponseHandler import ResponseHandler


import questionary


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