# Story about django scripts

## 2025-04-02

## Objective

- I want to learn django.
- Write automation scripts.

## Project Tree

Simple but organized.

```plaintext
C:\atari-monk\code\py-scripting
├── .gitignore
├── .vscode
│   └── launch.json
├── django_scripts
│   ├── __init__.py
│   ├── data
│   │   └── django_gitignore.txt
│   ├── docs
│   │   ├── historia.md
│   │   └── story.md
│   ├── generate_app.py
│   ├── generate_gitignore.py
│   ├── generate_project.py
│   ├── meta_model.py
│   ├── model_class.py
│   └── setup_django.py
└── index.md
```

## setup_django.py

- check if framework is installed
- print version if it is
- ask to update and update if user wants to
- install if not installed
- it needs to be able to be run any time and in bigger script when framework needs to be checked
- i skipped considering virtual environment/global and such stuff for now

## generate_project.py

- executes if django installed
- make files and project in root folder witch is a repo folder
- adds gitignore sections related to django proj
- it needs to be run standalone and in bigger script both
- it uses input if none or argparse for params form cli
- check if proj alerady there
- applay migrations optionaly
- run server optionaly, in new cli so it is independant

```sh
python -m django_scripts.generate_project C:\atari-monk\code linkshelf --gitignore-template C:\atari-monk\code\py-scripting\data\django_gitignore.txt
```

## generate_app.py

- generates app in django project

```sh
python -m django_scripts.generate_app -p linkshelf -a links -r C:\atari-monk\code\linkshelf
```

## 2025-04-04

- Refactor scripts to generate proj and app, in chosen repository

## 2025-04-05

## meta_model.py

- generate json representation of a data model
- currently not usefull, probably better to use ai

## model_class.py

- generate py class representation of a data model
- currently not usefull, probably better to use ai

## apply_model.py

- gets repo path, app name with argparse or input
- gets modle code from clipboard or file path
- appends model to app name/models.py
- updates project settings
- create and apply migrations
