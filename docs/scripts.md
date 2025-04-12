# Scripts

Python Scripts Module

## markdown_to_text.py

- takes markdown from clipboard
- converts it to plain text
- places it back in clipboard
- option to remove code sections

## remove_comments.py

- removeing comments from py file and save it back
- one function handles just one type of comments
- get file path from argparse or input

Py comments are really complex, they have many structures.  
AI generated solutions was failing.  
I started from simplest case file.  
Simplest function to remove simplest comment.  
I runned script to test it and generated unittest.  
I dont want to use re or any library, just simple text processing.  
Input and output clearly shows what comments can be cleared.  
There is many exeptions so i detect them and skip such cases.  
If it is not simple it wont work.

## fs_tree.py

- file system tree printout of folders and files in path
- get file path from argparse or input
- saved in md file and clipboard

## remove_folder_content.py

- removes folder content

## voice_to_text.py

- tests mic
- records mic, returns speach to text
