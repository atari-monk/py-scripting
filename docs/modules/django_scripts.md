# Django Scripts

Python Scripts Module for Django.  
Learn django and write automation scripts for it.

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

to run in cli:

```sh
python -m django_scripts.generate_project C:\atari-monk\code proj_name --gitignore-template C:\atari-monk\code\py-scripting\docs\data\django_gitignore.txt
```

## generate_app.py

- generates app in django project

to run in cli:

```sh
python -m django_scripts.generate_app -p proj_name -a app_name -r C:\atari-monk\code\proj_name
```

- Scripts generate proj and app, in chosen repository

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
