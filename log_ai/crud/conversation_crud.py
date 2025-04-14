import os
from log_ai.model.config import DB
from log_ai.model.conversation import Conversation
from log_ai.crud.crud import CRUD
from shared_library.json_file_storage import JSONFileStorage

class ConversationCRUD(CRUD):
    def __init__(self):
        storage = JSONFileStorage(file_path=os.path.join(DB, 'conversations.json'))
        super().__init__(model=Conversation, storage=storage)
