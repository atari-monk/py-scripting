import os
from log_project.model.config import DB
from log_project2.model.Project import Project
from shared_library.json_repository import JSONRepository
from shared_library.jsonl_file_storage import JSONLFileStorage

class ProjectCRUDJsonl(JSONRepository):
    def __init__(self):
        storage = JSONLFileStorage(file_path=os.path.join(DB, 'projects2.jsonl'))
        super().__init__(model=Project, storage=storage)