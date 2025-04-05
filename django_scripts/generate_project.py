import os
import sys
import subprocess
import argparse
import re
from typing import Optional
from django_scripts.generate_gitignore import ensure_gitignore
from django_scripts.setup_django import get_django_version

def generate_project(
    repo_path: Optional[str] = None,
    project_name: Optional[str] = None,
    skip_migrations: bool = False,
    skip_runserver: bool = False,
    gitignore_template_path: Optional[str] = None
) -> None:
    if repo_path is None:
        repo_path = input("Enter the parent directory for the project: ").strip()
        if not repo_path:
            print("Error: Repository path cannot be empty.")
            sys.exit(1)

    if project_name is None:
        while True:
            project_name = input("Enter the Django project name (letters, numbers, and underscores only): ").strip()
            if not project_name:
                print("Error: Project name cannot be empty.")
                continue
            if not is_valid_project_name(project_name):
                print("Error: Project name can only contain letters, numbers, and underscores, and cannot start with a number.")
                continue
            break
    else:
        if not is_valid_project_name(project_name):
            print("Error: Project name can only contain letters, numbers, and underscores, and cannot start with a number.")
            sys.exit(1)

    os.makedirs(repo_path, exist_ok=True)
    repo_path = os.path.abspath(repo_path)
    
    project_dir = os.path.join(repo_path, project_name)
    if os.path.exists(os.path.join(project_dir, 'manage.py')):
        print(f"Error: Django project files already exist in '{project_dir}'.")
        sys.exit(1)

    print(f"Generating Django project '{project_name}' in directory '{repo_path}'...")
    try:
        subprocess.run(
            ['django-admin', 'startproject', project_name],
            check=True,
            cwd=repo_path
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating project: {e}")
        sys.exit(1)

    ensure_gitignore(project_dir, gitignore_template_path)

    if not skip_migrations:
        print("Applying migrations...")
        manage_py = os.path.join(project_dir, 'manage.py')
        subprocess.run([sys.executable, manage_py, 'migrate'], check=True, cwd=project_dir)

    if not skip_runserver:
        print("Starting development server...")
        manage_py = os.path.join(project_dir, 'manage.py')
        if sys.platform == 'win32':
            subprocess.Popen(
                ['start', 'cmd', '/k', sys.executable, manage_py, 'runserver'],
                shell=True,
                cwd=project_dir
            )
        else:
            subprocess.Popen(
                [sys.executable, manage_py, 'runserver'],
                cwd=project_dir
            )

    print(f"\nSuccessfully created Django project '{project_name}' in directory '{project_dir}'")
    if not skip_runserver:
        print("Development server is running in a separate window.")

def is_valid_project_name(name: str) -> bool:
    return re.match(r'^[_a-zA-Z][_a-zA-Z0-9]*$', name) is not None

def main():
    if get_django_version() is None:
        print("Error: Django is not installed. Please install Django before running this script.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Generate a new Django project in the specified directory.')
    parser.add_argument('repo_path', nargs='?', help='Parent directory where project will be created')
    parser.add_argument('project_name', nargs='?', help='Name of the Django project')
    parser.add_argument('--skip-migrations', action='store_true', help='Skip applying initial migrations')
    parser.add_argument('--skip-runserver', action='store_true', help='Skip running the development server')
    parser.add_argument('--gitignore-template', help='Path to a custom .gitignore template file')

    args = parser.parse_args()
    generate_project(
        repo_path=args.repo_path,
        project_name=args.project_name,
        skip_migrations=args.skip_migrations,
        skip_runserver=args.skip_runserver,
        gitignore_template_path=args.gitignore_template
    )

if __name__ == '__main__':
    main()