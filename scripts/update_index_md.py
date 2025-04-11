import os
import argparse
from pathlib import Path

def clean_name(name):
    return name.replace('_', ' ').replace('-', ' ').title().strip()

def generate_docs_index(repo_path):
    repo_path = Path(repo_path).resolve()
    docs_path = repo_path / 'docs'
    index_file = repo_path / 'index.md'
    
    if not docs_path.exists():
        print(f"Error: 'docs' folder not found in {repo_path}")
        return
    
    index_content = ["# Documentation Index\n"]
    
    for root, dirs, files in os.walk(docs_path):
        if Path(root) == docs_path:
            continue
            
        md_files = [f for f in files if f.lower().endswith('.md')]
        if not md_files:
            continue
            
        rel_path = Path(root).relative_to(docs_path)
        section_name = clean_name(rel_path.name)
        index_content.append(f"\n## {section_name}")
        
        for file in md_files:
            file_path = Path(root) / file
            rel_file_path = file_path.relative_to(repo_path)
            name = clean_name(file_path.stem)
            index_content.append(f"- [{name}]({str(rel_file_path).replace('\\', '/')})")
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))
    
    print(f"Generated index with {len(index_content) - 1} sections in {index_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate documentation index from docs folder')
    parser.add_argument('path', nargs='?', help='Path to repository root directory')
    args = parser.parse_args()
    
    repo_path = args.path if args.path else input("Enter repository path: ").strip()
    if not repo_path:
        print("Error: No repository path provided")
        return
    
    generate_docs_index(repo_path)

if __name__ == '__main__':
    main()