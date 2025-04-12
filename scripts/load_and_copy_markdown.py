import argparse
import os
import pyperclip

def load_and_copy_markdown(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path: {folder_path}")
        return
    
    md_files = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                md_files[filename] = file.read()
    
    if not md_files:
        print("No markdown files found in the folder.")
        return
    
    print("Loaded Markdown files:")
    for i, filename in enumerate(md_files.keys(), start=1):
        print(f"{i}. {filename}")
    
    try:
        selected_index = int(input("Enter the number of the markdown file to load: ")) - 1
        if 0 <= selected_index < len(md_files):
            selected_filename = list(md_files.keys())[selected_index]
            pyperclip.copy(md_files[selected_filename])
            print(f"Copied '{selected_filename}' to clipboard.")
        else:
            print("Invalid number selected.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    parser = argparse.ArgumentParser(description='Load and copy markdown files from a folder.')
    parser.add_argument('--folder', '-f', help='Path to the folder containing markdown files')
    
    args = parser.parse_args()
    
    if args.folder:
        folder_path = args.folder
    else:
        folder_path = input("Enter the path to the folder containing markdown files: ")
    
    load_and_copy_markdown(folder_path)

if __name__ == "__main__":
    main()