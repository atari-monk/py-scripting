import json
import os
import logging
from .i_storage import IStorage

logger = logging.getLogger(__name__)

class JSONLFileStorage(IStorage):
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.save_all([])

    def load_all(self, model):
        instances = []
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    instances.append(model.from_dict(data))
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Error reading from {self.file_path}: {e}")
        return instances

    def save_all(self, instances):
        try:
            with open(self.file_path, 'w') as f:
                for instance in instances:
                    json_line = json.dumps(instance.to_dict())
                    f.write(json_line + '\n')
            logger.info(f"Data successfully written to {self.file_path}")
        except IOError as e:
            logger.error(f"Error writing to {self.file_path}: {e}")

    def append(self, instance):
        try:
            with open(self.file_path, 'a') as f:
                f.write(json.dumps(instance.to_dict()) + "\n")
            logger.info(f"Appended data to {self.file_path}")
        except IOError as e:
            logger.error(f"Error appending to {self.file_path}: {e}")
