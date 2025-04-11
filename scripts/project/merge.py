import os
import sys

def get_files_file_extensions():
    return ['.json', '.html', '.js', '.css', '.ts', '.py']

def get_ignored_items():
    project_groups = [
        [".git", "script", "node_modules", "dist", "build"],
        ["__pycache__"],
    ]

    file_groups = [
        ["package-lock.json"],
        ["__init__.py"],
    ]
    
    return {
        "projects": {item for group in project_groups for item in group},
        "files": {item for group in file_groups for item in group}
    }

def get_files_to_merge(project_folder, file_extensions, ignored_projects, ignored_files):
    for root, dirs, files in os.walk(project_folder):
        dirs[:] = [d for d in dirs if d not in ignored_projects]
        for file in files:
            if file in ignored_files:
                continue
            if any(file.endswith(ext) for ext in file_extensions):
                yield os.path.join(root, file)

def write_md_file(file_paths, project_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for file_path in file_paths:
            rel_path = os.path.relpath(file_path, project_folder)
            f.write(f"### {rel_path}\n\n```typescript\n")
            try:
                with open(file_path, "r", encoding="utf-8") as file_content:
                    content = file_content.read()
                f.write(f"{content}\n\n")
            except Exception as e:
                f.write(f"Could not read file content: {e}\n\n")
            f.write("```\n\n")

def write_txt_file(file_paths, project_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for file_path in file_paths:
            rel_path = os.path.relpath(file_path, project_folder)
            f.write(f"File: {rel_path}\n")
            try:
                with open(file_path, "r", encoding="utf-8") as file_content:
                    content = file_content.read()
                f.write(f"{content}\n\n")
            except Exception as e:
                f.write(f"Could not read file content: {e}\n\n")

def merge(project_folder):
    if not os.path.isdir(project_folder):
        print("The provided path is not valid. Exiting.")
        return

    ignored_items = get_ignored_items()
    ignored_projects = ignored_items["projects"]
    ignored_files = ignored_items["files"]
    file_extensions = get_files_file_extensions()
    
    try:
        file_paths = list(get_files_to_merge(project_folder, file_extensions, ignored_projects, ignored_files))

        output_file_txt = os.path.join(project_folder, "merge.txt")
        write_txt_file(file_paths, project_folder, output_file_txt)
        print(f"Text file saved to: {output_file_txt}")

        output_file_md = os.path.join(project_folder, "merge.md")
        write_md_file(file_paths, project_folder, output_file_md)
        print(f"Markdown file saved to: {output_file_md}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting gracefully.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <project_folder_path>")
        sys.exit(1)
    
    project_folder = sys.argv[1]
    merge(project_folder)