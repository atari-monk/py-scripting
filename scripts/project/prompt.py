import pyperclip
import os

def read_code_files(file_paths):
    code_contents = []
    for path in file_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                code_contents.append(f"### File: {path}\n{file.read()}\n")
        else:
            print(f"Warning: {path} does not exist.")
    return "\n".join(code_contents)

def generate_prompt():
    print("Enter paths to the code files (comma-separated):")
    file_paths = input().strip().split(",")
    file_paths = [path.strip() for path in file_paths]
    
    print("Enter your prompt for refactoring:")
    user_prompt = input().strip()
    
    code_context = read_code_files(file_paths)
    
    full_prompt = f"""
    Refactor the following code based on this request:
    {user_prompt}
    
    {code_context}
    """.strip()
    
    pyperclip.copy(full_prompt)
    print("Prompt copied to clipboard! Paste it into your AI tool.")

if __name__ == "__main__":
    generate_prompt()
