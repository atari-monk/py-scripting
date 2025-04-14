import os
from log_project.model.config import DB
from log_project2.model.Project import Project
from shared_library.json_file_storage import JSONFileStorage
from shared_library.json_repository import JSONRepository

class ProjectCRUD(JSONRepository):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'projects2.json'))
        super().__init__(model=Project, storage=storage)

