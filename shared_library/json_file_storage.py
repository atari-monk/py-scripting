import json
import os
import logging
from .i_storage import IStorage

logger = logging.getLogger(__name__)

class JSONFileStorage(IStorage):
    def __init__(self, file_path: str, indent: int = 2):
        self.file_path = file_path
        self.indent = indent
        if not os.path.exists(self.file_path):
            self.save_all([])

    def load_all(self, model):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [model.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Error reading from {self.file_path}: {e}")
            return []

    def save_all(self, instances):
        try:
            with open(self.file_path, 'w') as f:
                json.dump([instance.to_dict() for instance in instances], f, indent=self.indent)
            logger.info(f"Data successfully written to {self.file_path}")
        except IOError as e:
            logger.error(f"Error writing to {self.file_path}: {e}")

    def append(self, instance):
        raise NotImplementedError("Appending is not supported for JSON format.")
    