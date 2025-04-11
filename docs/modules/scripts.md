# scripts module Story

## 2025-04-03

### markdown_to_text.py

- takes markdown from clipboard
- converts it to plain text
- places it back in clipboard

### remove_comments.py

- removeing comments from py file and save it back
- one function handles just one type of comments
- get file path from argparse or input

- THIS GAVE ME IMMENSE PROBLEM
- py comments are really complex, they have many structures
- ai generated solutions was failing
- i started from simplest case file
- simplest function to remove simplest comment
- i runned script to test it and generated unittest
- i dont want to use re or any library, just simple text processing
- input and output clearly shows what comments can be cleared
- there is many exeptions so i detect them and skip such cases
- if it is not simple it wont work

### tests in py

- want to setup unit tests in py
- test_remove_comments.py
- to run:

```sh
python -m unittest .\tests\test_remove_comments.py
```

- debuged with VSCODE launch.json

### fs_tree.py

- file system tree printout of folders and files in path
- get file path from argparse or input
- saved in md file and clipboard

## 2025-04-05

### remove_folder_content.py

- removes folder content

## 2025-04-07

### markdown_to_text.py

- menu option to remove code sections

### voice_to_text.py

- tests mic
- records mic, returns speach to text
