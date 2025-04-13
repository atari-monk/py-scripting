from enum import Enum
from typing import List

class ValidatorEnum:
    @staticmethod
    def validate_enum_by_list(value: str, allowed_values: List[str]) -> str:
        if value not in allowed_values:
            raise ValueError(f"Value must be one of the following: {', '.join(allowed_values)}.")
        return value

    @staticmethod
    def validate_enum_by_class(value: str, enum_class: Enum) -> str:
        allowed_values = [e.value for e in enum_class]
        if value not in allowed_values:
            raise ValueError(f"Value must be one of the following: {', '.join(allowed_values)}.")
        return value
