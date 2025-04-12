# py-scripting

Repository containing Python scripts for automation and joy.

## Philosophy

### On Wrappers

Avoid writing scripts to run other scripts. Instead:

- Write focused, well-designed scripts
- Use the CLI directly to run scripts
- Leverage existing packages rather than creating wrappers

I've learned from experience that creating menu systems or script runners is generally:

- A maintenance burden
- Unnecessary when CLI tools exist
- Often better handled by proper packaging

## Repository Structure

### Root Directory

- `setup.py` (Python package configuration)
- `requirements.txt` (dependencies)
- `__init__.py` (enables repo as Python module)
- `.gitignore`
- `.vscode/` (editor configuration)
- `docs/` (documentation for GitHub Pages)
- `py_scripting.egg-info/` (generated package metadata, excluded from version control)
- Python modules and project files

### Documentation Standards

- Single `docs/` directory containing all Markdown documentation
- Documentation must be strictly relevant to the repository's content
- Automatically update `index.md` using:
  ```sh
  python ./scripts/update_index_md.py
  ```

## Testing

- Unit tests written in Python
- Debugged using VS Code's `launch.json` configurations
- Tests reside in `tests/` directory
- To run tests:
  ```sh
  python -m unittest ./tests/test_remove_comments.py
  ```
