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
C:\atari-monk\code\learn-django
├── docs
│   └── story.md
├── index.md
└── script
    ├── generate_project.py
    └── setup_django.py
```

## Setup django

- I want a script 'setup_django.py' that will:
- check if framework is installed
- print version if it is
- ask to update and update if user wants to
- install if not installed
- it needs to be able to be run any time and in bigger script when framework needs to be checked
- i skipped considering virtual environment/global and such stuff for now
- tested

## They way of using scripts

- This is very important
- In root folder is script folder
- I run scripts with

```sh
 python .\script\setup_django.py
```

- cleaing console with

```sh
cls
```

- Many a times i wrote wrappers with menus to run scripts
- This run script wrappers made me loose the plot every time
- DONT DO THEM UNLESS MUCH LATER AT MATURITY OF SCRIPTS
- also i dont want to use subprocess to run them scripts in batch, better keep it one by one
- run one script and process changes, is a fine rule

## Generate project

- I want a script to generate django project 'generate_project.py'
- script is in root/script
- make files and project in root
- adds gitignore sections related to django proj
- it needs to be run standalone and in bigger script both
- has header: def generate_project(project_name=None, skip_migrations=False, skip_runserver=False):
- it uses input if none or argparse for params form cli
- check if proj alerady there
- applay migrations optionaly
- run server optionaly, in new cli so it is independant
- usage:

```sh
python .\script\generate_project.py myproject
```

or optionaly:

```sh
python .\script\generate_project.py myproject --skip-migrations --skip-runserver
```

- tested

## .gitignore

- ignored 'linkshelf' project while testing scripts
- ignored 'helpers' folder with some temporary helping utility scripts
- ignored 'manage.py' from django test proj

## Delete test proj

- script 'delete_project.py' removes db.sqlite3, linkshelf, manage.py
- tested

## 2025-04-04

## Generate model

- script 'meta_model.py'
- generate json representation of a data model
- script 'model_class.py'
- generate py class representation of a data model

## Refactor scripts to generate in chosen repository
