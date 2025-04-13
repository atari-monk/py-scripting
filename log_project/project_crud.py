import os
from log_project.config import DB
from log_project.project import Project
from log_project.project2 import Project2
from shared_library.json_file_storage import JSONFileStorage
from shared_library.json_repository import JSONRepository
from shared_library.jsonl_file_storage import JSONLFileStorage

class ProjectCRUD(JSONRepository):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'projects.json'))
        super().__init__(model=Project, storage=storage)

class ProjectCRUD2(JSONRepository):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'projects2.json'))
        super().__init__(model=Project2, storage=storage)

class ProjectCRUD3(JSONRepository):
    def __init__(self):
        storage = JSONLFileStorage(file_path=os.path.join(DB, 'projects2.jsonl'))
        super().__init__(model=Project2, storage=storage)