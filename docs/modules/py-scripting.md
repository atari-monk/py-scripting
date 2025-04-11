# py-scripting

Repo with py scripts.

## On Wrappers

Note to self: Do not write scripts to run scripts.  
Better write fine scripts.  
I had this silly tendency to write menus or runners.  
Pointless waste, there is cli console to run this.  
There is packages to do instead.

## Repo structure Assumptions

- Repo documents in root
  - setup.py
  - requirements.txt
  - index.md (for github pages on root)
  - \_\_init\_\_.py
  - .gitignore
  - .vscode
  - docs
  - py_scripting.egg-info (module data, not in source control)
- Py modules or projects in root
- One docs folder in repo
- All markdown docs in docs folder,
- docs has additionally
  - json (folder for json data)
  - task_db (folder for task_system api data storage)
  - docs

index.md is updated by script:

```sh
python 
```