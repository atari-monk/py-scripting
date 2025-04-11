import argparse
import os
import re
import sys
from pathlib import Path

def clean_name(name):
    return name.replace('_', ' ').replace('-', ' ').strip()

def generate_links(folder_path, target_file, section_name=None):
    folder_path = Path(folder_path).resolve()
    target_file = Path(target_file).resolve()
    
    if not section_name:
        default_name = clean_name(folder_path.name).title()
        section_name = input(f"Enter section name [{default_name}]: ").strip() or default_name
    
    md_files = list(folder_path.glob('**/*.md'))
    if not md_files:
        print(f"No markdown files found in {folder_path}")
        return
    
    processed_files = []
    for file in md_files:
        rel_path = os.path.relpath(file, target_file.parent)
        filename = file.stem
        
        match = re.match(r'^(\d+)[_\-]?(.*)', filename)
        if match:
            order = int(match.group(1))
            name = clean_name(match.group(2)) or clean_name(filename)
        else:
            order = float('inf')
            name = clean_name(filename)
        
        processed_files.append({
            'order': order,
            'name': name,
            'path': rel_path.replace('\\', '/')
        })
    
    processed_files.sort(key=lambda x: (x['order'], x['name'].lower()))
    
    links_section = [f"\n## {section_name}"] + [
        f"- [{f['name']}]({f['path']})" for f in processed_files
    ]
    
    mode = 'a' if target_file.exists() else 'w'
    with open(target_file, mode, encoding='utf-8') as f:
        f.write('\n'.join(links_section) + '\n')
    
    print(f"✅ Added {len(processed_files)} links under '{section_name}' in {target_file}")

def get_valid_path(prompt, is_file=False):
    """Prompt until valid path is entered"""
    while True:
        path = input(prompt).strip()
        if not path:
            continue
        path_obj = Path(path)
        if is_file:
            if path_obj.parent.exists():
                return path
        else:
            if path_obj.exists():
                return path
        print("Invalid path, please try again")

def main():
    parser = argparse.ArgumentParser(
        description="Generate markdown links to all .md files in a folder"
    )
    parser.add_argument('target', nargs='?', help="Target markdown file path")
    parser.add_argument('folder', nargs='?', help="Folder containing markdown files")
    parser.add_argument('-t', '--target', dest='target_alt', help="Alternative target file path")
    parser.add_argument('-f', '--folder', dest='folder_alt', help="Alternative folder path")
    parser.add_argument('-n', '--name', help="Section name for the links")
    
    args = parser.parse_args()
    
    target = args.target_alt or args.target
    folder = args.folder_alt or args.folder
    
    if not target and not folder:
        if len(sys.argv) > 1 and sys.argv[1].endswith('.md'):
            target = sys.argv[1]
            folder = get_valid_path("Path to markdown files folder: ") if len(sys.argv) < 3 else sys.argv[2]
        else:
            target = get_valid_path("Path to target markdown file: ", is_file=True)
            folder = get_valid_path("Path to markdown files folder: ")
    elif not folder:
        folder = get_valid_path("Path to markdown files folder: ")
    elif not target:
        target = get_valid_path("Path to target markdown file: ", is_file=True)
    
    generate_links(folder, target, args.name)

if __name__ == '__main__':
    main()