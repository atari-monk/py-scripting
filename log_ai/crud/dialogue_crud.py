import os
from log_ai.crud.crud import CRUD
from log_ai.model.config import DB
from log_ai.model.dialogue import Dialogue
from shared_library.json_file_storage import JSONFileStorage

class DialogueCRUD(CRUD):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'dialogs.json'))
        super().__init__(model=Dialogue, storage=storage)

    def get_dialogs_by_conversation_id(self, conversation_id: str):
        # Assuming you have a way to fetch dialogs by conversation_id
        # This could query a dialogs database or list where dialogs are stored
        dialogs = self.list_all()
        return [dialog for dialog in dialogs if dialog['conversation_id'] == conversation_id]
