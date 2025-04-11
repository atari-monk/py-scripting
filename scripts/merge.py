import os
import sys
import argparse

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

def merge(project_folder, generate_md=False):
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

        if generate_md:
            output_file_md = os.path.join(project_folder, "merge.md")
            write_md_file(file_paths, project_folder, output_file_md)
            print(f"Markdown file saved to: {output_file_md}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Merge project files into a single output file.')
    parser.add_argument('project_folder', nargs='?', help='Path to the project folder')
    parser.add_argument('-md', '--markdown', action='store_true', 
                       help='Generate markdown output in addition to text')
    
    args = parser.parse_args()
    
    if not args.project_folder:
        args.project_folder = input("Enter project folder path: ")
    
    merge(args.project_folder, args.markdown)

if __name__ == "__main__":
    main()