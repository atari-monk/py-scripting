import os
import subprocess
import re
import sys
import argparse
from typing import Optional

def generate_app(repo_path: Optional[str] = None,
    project_name: Optional[str] = None, 
    app_name: Optional[str] = None) -> None:
    if repo_path is None:
        repo_path = input("Enter the repository folder path for the project: ").strip()
        if not repo_path:
            print("Error: Repository path cannot be empty.")
            sys.exit(1)
    
    if project_name is None:
        project_name = input("📌 Enter your Django project name: ").strip()
    
    if not project_name:
        print("⚠️ Project name cannot be empty. Try again.")
        return
    
    project_path = repo_path
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print(f"❌ Django project not found at {project_path} (manage.py not found). Try again.")
        return
    
    if app_name is None:
        app_name = input("📌 Enter your Django app name: ").strip()
    
    if not app_name:
        print("⚠️ App name cannot be empty. Try again.")
        return

    app_path = os.path.join(project_path, app_name)

    if os.path.exists(app_path):
        print(f"⚠️ The app '{app_name}' already exists in {project_path}. Choose a different name.")
        return

    print(f"\n🚀 Creating Django app '{app_name}' in {project_path}...\n")

    try:
        os.chdir(project_path)
        subprocess.check_call(["python", "manage.py", "startapp", app_name])
        print(f"✅ Django app '{app_name}' created successfully!\n")

        settings_path = find_settings_file(project_path, project_name)
        if settings_path:
            add_app_to_installed_apps(settings_path, app_name)
        else:
            print("⚠️ Could not find settings.py to automatically update INSTALLED_APPS.")
            print("\n📌 Manual Step: Register your app in settings.py")
            print("Add the following line in the INSTALLED_APPS list:\n")
            print(f"    '{app_name}',\n")

    except subprocess.CalledProcessError:
        print("❌ An error occurred while creating the app.")
    except FileNotFoundError:
        print("❌ Python or Django is not installed. Make sure you have Django set up correctly.")

def find_settings_file(project_path: str, project_name: str) -> Optional[str]:
    """Locate the settings.py file in the Django project."""
    modern_settings = os.path.join(project_path, project_name, "settings.py")
    if os.path.exists(modern_settings):
        return modern_settings
    
    traditional_settings = os.path.join(project_path, "settings.py")
    if os.path.exists(traditional_settings):
        return traditional_settings
    
    return None

def add_app_to_installed_apps(settings_path: str, app_name: str) -> None:
    """Add the new app to INSTALLED_APPS in settings.py."""
    try:
        with open(settings_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            
            pattern = r'INSTALLED_APPS\s*=\s*\[([^\]]*)'
            match = re.search(pattern, content, re.DOTALL)
            
            if match:
                start_pos = match.start(1)
                end_pos = content.find(']', start_pos)
                
                if end_pos != -1:
                    new_app_entry = f"    '{app_name}',\n"
                    new_content = content[:start_pos] + match.group(1) + new_app_entry + content[end_pos:]
                    
                    f.seek(0)
                    f.write(new_content)
                    f.truncate()
                    
                    print(f"✅ Successfully added '{app_name}' to INSTALLED_APPS in {settings_path}\n")
                else:
                    raise ValueError("Could not find closing bracket for INSTALLED_APPS")
            else:
                raise ValueError("INSTALLED_APPS not found in settings.py")
                
    except Exception as e:
        print(f"⚠️ Could not automatically update INSTALLED_APPS: {str(e)}")
        print("\n📌 Manual Step: Register your app in settings.py")
        print("Add the following line in the INSTALLED_APPS list:\n")
        print(f"    '{app_name}',\n")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a new Django app within an existing project."
    )
    parser.add_argument(
        "-p", "--project", 
        help="Name of the Django project",
        required=False
    )
    parser.add_argument(
        "-a", "--app", 
        help="Name of the new app to create",
        required=False
    )
    parser.add_argument(
        "-r", "--repo", 
        help="Path to the repository containing the project",
        required=False
    )
    
    args = parser.parse_args()
    
    generate_app(
        project_name=args.project,
        app_name=args.app,
        repo_path=args.repo
    )

if __name__ == "__main__":
    main()