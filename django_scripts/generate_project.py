import os
import sys
import subprocess
import argparse
from typing import Optional

def generate_project(
    repo_path: Optional[str] = None,
    skip_migrations: bool = False,
    skip_runserver: bool = False,
    gitignore_template_path: Optional[str] = None
) -> None:
    if repo_path is None:
        repo_path = input("Enter the repository folder path for the project: ").strip()
        if not repo_path:
            print("Error: Repository path cannot be empty.")
            sys.exit(1)

    os.makedirs(repo_path, exist_ok=True)
    
    repo_path = os.path.abspath(repo_path)
    project_name = os.path.basename(repo_path)

    if os.path.exists(os.path.join(repo_path, 'manage.py')):
        print(f"Error: Django project files already exist in the repository directory.")
        sys.exit(1)

    print(f"Creating Django project '{project_name}' in directory '{repo_path}'...")
    try:
        subprocess.run(
            ['django-admin', 'startproject', project_name, repo_path],
            check=True,
            cwd=repo_path
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating project: {e}")
        sys.exit(1)

    ensure_gitignore(repo_path, gitignore_template_path)

    if not skip_migrations:
        print("Applying migrations...")
        manage_py = os.path.join(repo_path, 'manage.py')
        subprocess.run([sys.executable, manage_py, 'migrate'], check=True, cwd=repo_path)

    if not skip_runserver:
        print("Starting development server...")
        manage_py = os.path.join(repo_path, 'manage.py')
        if sys.platform == 'win32':
            subprocess.Popen(
                ['start', 'cmd', '/k', sys.executable, manage_py, 'runserver'],
                shell=True,
                cwd=repo_path
            )
        else:
            subprocess.Popen(
                [sys.executable, manage_py, 'runserver'],
                cwd=repo_path
            )

    print(f"\nSuccessfully created Django project '{project_name}' in directory '{repo_path}'")
    if not skip_runserver:
        print("Development server is running in a separate window.")

def ensure_gitignore(root_dir: str, gitignore_template_path: Optional[str] = None) -> None:
    gitignore_path = os.path.join(root_dir, '.gitignore')
    gitignore_content = get_gitignore_content(gitignore_template_path)

    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)
        return

    with open(gitignore_path, 'r') as f:
        existing_content = f.read()

    if "# Django" not in existing_content:
        with open(gitignore_path, 'a') as f:
            f.write("\n" + gitignore_content)

def get_gitignore_content(gitignore_template_path: Optional[str] = None) -> str:
    if gitignore_template_path and os.path.exists(gitignore_template_path):
        try:
            with open(gitignore_template_path, 'r') as f:
                return f.read()
        except IOError:
            print(f"Warning: Could not read gitignore template from {gitignore_template_path}, using default")

def main():
    parser = argparse.ArgumentParser(description='Generate a new Django project in the specified directory.')
    parser.add_argument('repo_path', nargs='?', help='Path to the repository folder where project will be created')
    parser.add_argument('--skip-migrations', action='store_true', help='Skip applying initial migrations')
    parser.add_argument('--skip-runserver', action='store_true', help='Skip running the development server')
    parser.add_argument('--gitignore-template', help='Path to a custom .gitignore template file')

    args = parser.parse_args()
    generate_project(
        repo_path=args.repo_path,
        skip_migrations=args.skip_migrations,
        skip_runserver=args.skip_runserver,
        gitignore_template_path=args.gitignore_template
    )

if __name__ == '__main__':
    main()