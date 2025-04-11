import pyperclip
import re
from typing import List, Optional

class Strings:
    MENU_PROMPT = "Select a category:"
    CATEGORY_INPUT_PROMPT = "Enter the number corresponding to the category: "
    INVALID_CHOICE = "Invalid choice. Please select a number from the menu."
    SCOPE_PROMPT = "Enter the scope (or leave blank for none): "
    INVALID_SCOPE = "Invalid scope. Use only letters, numbers, hyphens, underscores, or dots."
    DESCRIPTION_PROMPT = "Enter a short description of the change: "
    DESCRIPTION_INVALID = "Description is required and must be 50 characters or less."
    NOTES_PROMPT = "Enter additional notes (optional, press Enter to skip): "
    GENERATED_MESSAGE = "\nGenerated Commit Message:"
    GENERATED_MESSAGE_SEPARATOR = "-" * 30
    COPIED_TO_CLIPBOARD = "Commit message copied to clipboard!"
    INVALID_NUMBER = "Please enter a valid number."
    REGEX_SCOPE = r"^[a-zA-Z0-9-_.]*$"
    PROGRAM_START = "Git Commit Message Generator"
    CATEGORIES = ["feat", "fix", "chore", "docs", "style", "refactor", "test", "perf"]
    MAIN = "__main__"

def display_menu() -> List[str]:
    print(Strings.MENU_PROMPT)
    for i, category in enumerate(Strings.CATEGORIES, 1):
        print(f"{i}. {category}")
    return Strings.CATEGORIES

def get_category(categories: List[str]) -> str:
    while True:
        try:
            choice = int(input(Strings.CATEGORY_INPUT_PROMPT))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(Strings.INVALID_CHOICE)
        except ValueError:
            print(Strings.INVALID_NUMBER)

def get_scope() -> str:
    while True:
        scope = input(Strings.SCOPE_PROMPT)
        if re.match(Strings.REGEX_SCOPE, scope):
            return scope
        else:
            print(Strings.INVALID_SCOPE)

def get_description() -> str:
    while True:
        description = input(Strings.DESCRIPTION_PROMPT)
        if description and len(description) <= 50:
            return description
        else:
            print(Strings.DESCRIPTION_INVALID)

def get_notes() -> Optional[str]:
    notes = input(Strings.NOTES_PROMPT)
    return notes.strip() if notes.strip() else None

def format_commit_message(category: str, scope: str, description: str, notes: Optional[str]) -> str:
    scope_part = f"({scope})" if scope else ""
    header = f"{category}{scope_part}: {description}"
    body = notes if notes else ""
    return f"{header}\n\n{body}" if body else header

def commit_msg():
    print(Strings.PROGRAM_START)
    categories = display_menu()

    category = get_category(categories)
    scope = get_scope()
    description = get_description()
    notes = get_notes()

    commit_message = format_commit_message(category, scope, description, notes)

    print(Strings.GENERATED_MESSAGE)
    print(Strings.GENERATED_MESSAGE_SEPARATOR)
    print(commit_message)
    print(Strings.GENERATED_MESSAGE_SEPARATOR)

    pyperclip.copy(commit_message)
    print(Strings.COPIED_TO_CLIPBOARD)

if __name__ == "__main__":
    commit_msg()
