from typing import Dict, Optional
from task_system.api.MarkdownStorage import MarkdownStorage
from task_system.api.MemoryStorage import MemoryStorage
from .models import CodingTask

class TaskStorage:
    def __init__(self):
        self.memory = MemoryStorage()
        self.markdown = MarkdownStorage()

    def configure_markdown(self, md_folder: Optional[str], md_filename: str = "task.md"):
        self.markdown.configure(md_folder, md_filename)

    def create(self, task: CodingTask) -> CodingTask:
        memory_task = self.memory.create(task)

        if task.storage_config.md_folder:
            self.markdown.configure(
                task.storage_config.md_folder,
                task.storage_config.md_filename
            )
            self.markdown.create(task)

        return memory_task

    def read(self, task_id: str) -> Optional[dict]:
        task = self.memory.read(task_id)
        if task:
            return task

        if self.markdown.enabled:
            return self.markdown.read(task_id)

        return None

    def update(self, task_id: str, task: CodingTask) -> Optional[CodingTask]:
        updated = self.memory.update(task_id, task)
        if not updated:
            return None

        if task.storage_config.md_folder:
            self.markdown.configure(
                task.storage_config.md_folder,
                task.storage_config.md_filename
            )
            self.markdown.update(task_id, task)

        return updated

    def list_all(self) -> Dict[str, dict]:
        tasks = self.memory.list_all()

        if self.markdown.enabled:
            md_tasks = self.markdown.list_all()
            for task_id, task_data in md_tasks.items():
                if task_id not in tasks:
                    tasks[task_id] = task_data

        return tasks
