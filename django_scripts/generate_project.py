import os
import sys
import subprocess
import argparse
from typing import Optional

def ensure_gitignore(root_dir: str) -> None:
    gitignore_path = os.path.join(root_dir, '.gitignore')
    gitignore_content = """# Django
*.sqlite3
*.pyc
__pycache__/
*.log
*.pot
*.py[co]
*.sw[nop]
*~
/.venv/
.env
.venv/
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.idea/
.vscode/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Static files
staticfiles/
mediafiles/
"""

    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)
        return

    with open(gitignore_path, 'r') as f:
        existing_content = f.read()

    if "# Django" not in existing_content:
        with open(gitignore_path, 'a') as f:
            f.write("\n" + gitignore_content)

def generate_project(project_name: Optional[str] = None, skip_migrations: bool = False, skip_runserver: bool = False) -> None:
    if project_name is None:
        project_name = input("Enter the Django project name: ").strip()
        if not project_name:
            print("Error: Project name cannot be empty.")
            sys.exit(1)

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if os.path.exists(os.path.join(root_dir, 'manage.py')):
        print(f"Error: Django project files already exist in root directory.")
        sys.exit(1)

    print(f"Creating Django project '{project_name}' in root directory...")
    try:
        subprocess.run(
            ['django-admin', 'startproject', project_name, root_dir],
            check=True,
            cwd=root_dir
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating project: {e}")
        sys.exit(1)

    ensure_gitignore(root_dir)

    if not skip_migrations:
        print("Applying migrations...")
        manage_py = os.path.join(root_dir, 'manage.py')
        subprocess.run([sys.executable, manage_py, 'migrate'], check=True, cwd=root_dir)

    if not skip_runserver:
        print("Starting development server...")
        manage_py = os.path.join(root_dir, 'manage.py')
        if sys.platform == 'win32':
            subprocess.Popen(
                ['start', 'cmd', '/k', sys.executable, manage_py, 'runserver'],
                shell=True,
                cwd=root_dir
            )
        else:
            subprocess.Popen(
                [sys.executable, manage_py, 'runserver'],
                cwd=root_dir
            )

    print(f"\nSuccessfully created Django project '{project_name}' in root directory")
    if not skip_runserver:
        print("Development server is running in a separate window.")

def main():
    parser = argparse.ArgumentParser(description='Generate a new Django project in root directory.')
    parser.add_argument('project_name', nargs='?', help='Name of the project to create')
    parser.add_argument('--skip-migrations', action='store_true', help='Skip applying initial migrations')
    parser.add_argument('--skip-runserver', action='store_true', help='Skip running the development server')

    args = parser.parse_args()
    generate_project(
        project_name=args.project_name,
        skip_migrations=args.skip_migrations,
        skip_runserver=args.skip_runserver
    )

if __name__ == '__main__':
    main()