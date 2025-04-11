# py-scripting

Repo with python scripts.

## On Wrappers

Note to self: Do not write scripts to run scripts.  
Better write fine scripts.  
I had this silly tendency to write menus or runners.  
Pointless waste, there is cli console to run this.  
There is packages to do instead.

## Repo structure Assumptions

- Repo files in root

  - setup.py
  - requirements.txt
  - index.md (for github pages on root)
  - \_\_init\_\_.py (repo is also py module)
  - .gitignore
  - .vscode
  - docs
  - py_scripting.egg-info (module data, not in source control)
  - Py modules and projects

- Docs

  - One docs folder in repo
  - All markdown docs in docs folder,
  - has additionally:
    - data (folder for data)
    - task_db (folder for task_system api data storage)
    - other folders with categories of md docs

  index.md is updated by script:

  ```sh
  python .\scripts\update_index_md.py
  ```
