import os
from log_project.model.ProjectTask import ProjectTask
from log_project.model.config import DB
from shared_library.json_file_storage import JSONFileStorage
from shared_library.json_repository import JSONRepository

class TaskCRUD(JSONRepository):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'tasks.json'))
        super().__init__(model=ProjectTask, storage=storage)
