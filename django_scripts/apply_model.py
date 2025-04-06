import argparse
import os
import sys
import pyperclip
from subprocess import call

def get_model_code(source):
    if source == 'clipboard':
        try:
            return pyperclip.paste()
        except Exception as e:
            print(f"Error accessing clipboard: {e}")
            sys.exit(1)
    else:
        try:
            with open(source, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading model file: {e}")
            sys.exit(1)

def append_to_models_file(app_path, model_code):
    models_path = os.path.join(app_path, 'models.py')
    
    if not os.path.exists(models_path):
        with open(models_path, 'w') as f:
            f.write("from django.db import models\n\n")
    
    with open(models_path, 'a') as f:
        f.write('\n\n' + model_code)
    
    print(f"Model code appended to {models_path}")

def run_migrations(repo_path):
    os.chdir(repo_path)
    
    print("\nCreating migrations...")
    call(['python', 'manage.py', 'makemigrations'])
    
    print("\nApplying migrations...")
    call(['python', 'manage.py', 'migrate'])

def main():
    parser = argparse.ArgumentParser(description='Apply Django model to an app')
    parser.add_argument('--repo', help='Path to Django project root')
    parser.add_argument('--app', help='Name of the Django app')
    parser.add_argument('--source', help='Source of model code (clipboard or file path)', default='clipboard')
    
    args = parser.parse_args()
    
    repo_path = args.repo or input("Enter path to Django project root: ")
    app_name = args.app or input("Enter Django app name: ")
    source = args.source
    
    repo_path = os.path.abspath(repo_path)
    app_path = os.path.join(repo_path, app_name)
    
    if not os.path.exists(app_path):
        print(f"Error: App directory not found at {app_path}")
        sys.exit(1)
    
    print("\nGetting model code...")
    model_code = get_model_code(source)
    print(f"Model code acquired from {'clipboard' if source == 'clipboard' else source}")
    
    print("\nUpdating models.py...")
    append_to_models_file(app_path, model_code)
    
    print("\nRunning migrations...")
    run_migrations(repo_path)
    
    print("\nDone!")

if __name__ == '__main__':
    main()