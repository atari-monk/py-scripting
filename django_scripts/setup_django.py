import subprocess
import sys
from typing import Optional

def get_django_version() -> Optional[str]:

    try:
        version = subprocess.check_output(
            [sys.executable, "-m", "django", "--version"],
            text=True,
            stderr=subprocess.PIPE
        ).strip()
        return version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def install_django() -> bool:

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
        print("\n✅ Django installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Failed to install Django. Please check your Python and pip installation.")
        return False

def update_django() -> bool:

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "django"])
        print("\n✅ Django updated successfully!")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Failed to update Django.")
        return False

def prompt_user(prompt: str) -> bool:

    while True:
        response = input(prompt + " (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")

def setup_django() -> bool:

    print("\n🚀 Checking Django setup...")

    version = get_django_version()

    if version is not None:
        print(f"\n✅ Django is installed (version: {version})")

        if prompt_user("\nWould you like to check for updates and install the latest version?"):
            if update_django():
                version = get_django_version()
                print(f"\n✅ Django updated to version: {version}")
            else:
                print("\n⚠️ Continuing with existing version.")
        return True
    else:
        print("\n❌ Django is not installed.")
        if prompt_user("\nWould you like to install Django now?"):
            if install_django():
                version = get_django_version()
                print(f"\n✅ Django installed successfully (version: {version})")
                return True
            else:
                print("\n❌ Django installation failed.")
                return False
        else:
            print("\n⚠️ Django installation skipped.")
            return False

if __name__ == "__main__":
    setup_django()