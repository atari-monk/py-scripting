import os

def get_base_folder():
    base_folder = input("Enter the path to the base folder: ")
    if not os.path.isdir(base_folder):
        print("The provided path is not valid. Exiting.")
        return None
    return base_folder

def get_ignored_projects():
    return {".git", "script", "node_modules", "dist", "build"}

def get_ignored_files():
    return {"package-lock.json"}

def list_available_folders(base_folder, ignored_projects):
    return [
        f for f in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, f)) and f not in ignored_projects
    ]

def choose_project_folder(subfolders):
    if not subfolders:
        print("No available project folders found.")
        return None
    for idx, folder in enumerate(subfolders, 1):
        print(f"{idx}: {folder}")
    choice = input("Enter the number corresponding to the project folder: ")
    try:
        return subfolders[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Exiting.")
        return None

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

def merge():
    base_folder = get_base_folder()
    if not base_folder:
        return
    ignored_projects = get_ignored_projects()
    ignored_files = get_ignored_files()
    subfolders = list_available_folders(base_folder, ignored_projects)
    selected_folder = choose_project_folder(subfolders)
    if not selected_folder:
        return
    project_folder = os.path.join(base_folder, selected_folder)
    file_extensions = ['.json', '.html', '.js', '.css', '.ts']
    file_paths = list(get_files_to_merge(project_folder, file_extensions, ignored_projects, ignored_files))

    output_file_txt = os.path.join(project_folder, "merge.txt")
    write_txt_file(file_paths, project_folder, output_file_txt)
    print(f"Text file saved to: {output_file_txt}")

    output_file_md = os.path.join(project_folder, "merge.md")
    write_md_file(file_paths, project_folder, output_file_md)
    print(f"Markdown file saved to: {output_file_md}")
    
if __name__ == "__main__":
    merge()
