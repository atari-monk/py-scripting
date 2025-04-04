# Story about django

## 2025-04-02

## Objective

- I want to learn django.
- Write automation scripts.
- This is second version of repo after first one was to complex
- This story is writen by hand (no ai), to keep me in context and to keep it simple as i can (i drift)

## Project Tree

See structure and keep it simple but organized.

```plaintext
C:\atari-monk\code\py-scripting
├── .gitignore
├── .vscode
│   └── launch.json
├── django_scripts
│   ├── __init__.py
│   ├── data
│   │   └── django_gitignore.txt
│   ├── delete_project.py
│   ├── docs
│   │   ├── historia.md
│   │   └── story.md
│   ├── generate_project.py
│   ├── meta_model.py
│   ├── model_class.py
│   └── setup_django.py
└── index.md
```

## Setup django

- I want a script 'setup_django.py' that will:
- check if framework is installed
- print version if it is
- ask to update and update if user wants to
- install if not installed
- it needs to be able to be run any time and in bigger script when framework needs to be checked
- i skipped considering virtual environment/global and such stuff for now

## They way of using scripts

- This is very important
- In root folder are scripts folders: root/scripts, ..., root/django_scripts
- Many a times i wrote wrappers with menus to run scripts
- This run script wrappers made me loose the plot every time
- DONT DO THEM UNLESS MUCH LATER AT MATURITY OF SCRIPTS
- also i dont want to use subprocess to run them scripts in batch, better keep it one by one
- run one script and process changes, is a fine rule

## Generate project

- I want a script to generate django project 'generate_project.py'
- executes if django installed
- make files and project in root folder witch is a repo folder
- adds gitignore sections related to django proj
- it needs to be run standalone and in bigger script both
- it uses input if none or argparse for params form cli
- check if proj alerady there
- applay migrations optionaly
- run server optionaly, in new cli so it is independant

## Delete test proj

- script 'delete_project.py' removes db.sqlite3, linkshelf, manage.py

## 2025-04-04

## Refactor scripts to generate in chosen repository

- 'generate_project.py'

```sh
python -m django_scripts.generate_project C:\atari-monk\code\linkshelf --gitignore-template C:\atari-monk\code\py-scripting\data\django_gitignore.txt
```

- 'generate_app.py'

```sh
python -m django_scripts.generate_app -p linkshelf -a links -r C:\atari-monk\code\linkshelf
```

## 2025-04-05

## Generate model

- script 'meta_model.py'
- generate json representation of a data model
- script 'model_class.py'
- generate py class representation of a data model
