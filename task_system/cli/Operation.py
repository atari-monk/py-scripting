from enum import Enum, auto


class Operation(Enum):
    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
    LIST = auto()
    QUIT = auto()