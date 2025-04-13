from typing import Optional

class Validator:
    @staticmethod
    def validate_length(value: str, min_len: int = 3, max_len: int = 50) -> str:
        if not min_len <= len(value) <= max_len:
            raise ValueError(f"Value must be between {min_len} and {max_len} characters.")
        return value.strip()

    @staticmethod
    def validate_format(value: str) -> str:
        if not all(c.isalnum() or c.isspace() or c in "-_" for c in value):
            raise ValueError("Value must contain only alphanumeric characters, spaces, hyphens, and underscores.")
        return value.strip()

    @staticmethod
    def validate_word_count(value: str, min_words: int = 1) -> str:
        if len(value.split()) < min_words:
            raise ValueError(f"Value should contain at least {min_words} word(s).")
        return value.strip()

    @staticmethod
    def validate_enum(value: Optional[str], allowed_values: list) -> str:
        if value not in allowed_values:
            raise ValueError(f"Value must be one of the following: {', '.join(allowed_values)}.")
        return value
    
    @staticmethod
    def validate_name(name: str, min_len: int = 3, max_len: int = 50) -> str:
        name = Validator.validate_length(name, min_len, max_len)
        name = Validator.validate_format(name)
        return Validator.validate_word_count(name)

    @staticmethod
    def validate_description(description: str, min_len: int = 10, min_words: int = 1) -> str:
        description = Validator.validate_length(description, min_len)
        description = Validator.validate_format(description)
        description = Validator.validate_word_count(description, min_words)
        return description.strip()
