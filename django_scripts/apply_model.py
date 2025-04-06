import argparse
import os
import sys
import pyperclip
import re
from subprocess import call

def clean_string(s):
    return s.strip().replace('\r\n', '\n')

def get_model_code(source):
    if source == 'clipboard':
        try:
            return clean_string(pyperclip.paste())
        except Exception as e:
            print(f"Error accessing clipboard: {e}")
            sys.exit(1)
    else:
        try:
            with open(source, 'r') as f:
                return clean_string(f.read())
        except Exception as e:
            print(f"Error reading model file: {e}")
            sys.exit(1)

def is_likely_django_model(code):
    patterns = [
        r'class\s+\w+\s*\(.*models\.Model',
        r'class\s+\w+\s*\(.*\)\s*:\s*\n\s*.*models\.',
        r'from\s+django\.db\s+import\s+models',
        r'^\s*\w+\s*=\s*models\.\w+Field\s*\('
    ]
    
    code = code.strip()
    if not code:
        return False
    
    for pattern in patterns:
        if re.search(pattern, code, re.MULTILINE):
            return True
    
    return False

def append_to_models_file(app_path, model_code):
    models_path = os.path.join(app_path, 'models.py')
    print(f"Models path: {models_path}")
    
    if not os.path.exists(models_path):
        with open(models_path, 'w') as f:
            pass
    
    model_code = model_code.strip()
    model_code = model_code.strip().replace('\r\n', '\n')
    
    print(f"Model code: {model_code}")

    with open(models_path, 'a') as f:
        f.write('\n' + model_code + '\n')

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
    
    if not model_code:
        print("Error: Model code is empty. Please provide valid model code.")
        sys.exit(1)
    if not is_likely_django_model(model_code):
        print("Error: The provided code does not appear to be a Django model.")
        sys.exit(1)
    
    print(f"Model code acquired from {'clipboard' if source == 'clipboard' else source}")
    
    print("\nUpdating models.py...")
    append_to_models_file(app_path, model_code)
    
    print("\nRunning migrations...")
    run_migrations(repo_path)
    
    print("\nDone!")

if __name__ == '__main__':
    main()