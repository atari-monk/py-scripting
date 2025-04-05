import os
import argparse
from typing import Optional

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
            return get_default_gitignore_content()
    return get_default_gitignore_content()

def get_default_gitignore_content() -> str:
    return """# Django

        _.sqlite3
        _.pyc
        **pycache**/
        _.log
        _.pot
        _.py[co]
        _.sw[nop]
        \*~
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
        _.suo
        _.ntvs\*
        _.njsproj
        _.sln
        \*.sw?

        # Static files

        staticfiles/
        mediafiles/
    """

def main():
    parser = argparse.ArgumentParser(description='Generate a new gitignore file in the specified directory.')
    parser.add_argument('repo_path', nargs='?', help='Path to the repository folder where file will be generated')
    parser.add_argument('--gitignore-template', help='Path to a custom .gitignore template file')

    args = parser.parse_args()
    ensure_gitignore(args.repo_path, args.gitignore_template)

if __name__ == '__main__':
    main()