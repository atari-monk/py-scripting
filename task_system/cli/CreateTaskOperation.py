import questionary
from task_system.api.models import get_language_list
from task_system.cli.InputHandler import InputHandler
from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.ResponseHandler import ResponseHandler

class CreateTaskOperation(OperationStrategy):
    def execute(self) -> None:
        print("\n=== Create New Task ===")
        task_data = {
            "title": questionary.text("Title:").ask(),
            "description": questionary.text("Description:").ask(),
            "requirements": InputHandler.prompt_list("Requirements (one per line, empty to finish):"),
            "language": questionary.select(
                "Language:",
                choices=get_language_list()
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

        if questionary.confirm("Configure storage options?").ask():
            storage_config = {
                "md_folder": questionary.text(
                    "Markdown folder path (leave empty for default):",
                    default=""
                ).ask() or None,
                "md_filename": questionary.text(
                    "Markdown filename:",
                    default="task.md"
                ).ask()
            }
            task_data["storage_config"] = storage_config
            
        response = self.client.create_task(task_data)
        ResponseHandler.handle(response, "Task created successfully!")