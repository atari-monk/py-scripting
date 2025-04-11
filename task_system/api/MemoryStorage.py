from typing import Dict, Optional
from task_system.api.models import CodingTask

class MemoryStorage:
    def __init__(self):
        self.db = {}

    def create(self, task: CodingTask) -> CodingTask:
        self.db[task.id] = task.model_dump()
        return task

    def read(self, task_id: str) -> Optional[dict]:
        return self.db.get(task_id)

    def update(self, task_id: str, task: CodingTask) -> Optional[CodingTask]:
        if task_id not in self.db:
            return None
        self.db[task_id] = task.model_dump()
        return task

    def list_all(self) -> Dict[str, dict]:
        return self.db.copy()