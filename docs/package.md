# Python Local Package

## Import problem

How to make imports work in repo project ?  
Make repo a py module

```sh
pip install setuptools
```

Put \_\_init\_\_.py and setup.py in root

```py
#setup.py

from setuptools import setup, find_packages

setup(
    name="py_scripting",
    version="0.1",
    packages=find_packages(),
)
```

```sh
pip install -e .
```

Verify the Installation Worked

```sh
pip list | findstr py_scripting  # Windows
# or
pip list | grep py_scripting     # Linux/Mac
```

Check Your Python Environment

```
python -c "import sys; print(sys.executable)"
```

Now you can import cleanly from anywhere:

```py
from py_scripting.selenium_scripts.chatgpt import initialize_chatgpt_session
```

When You Would Need to Reinstall:
If you add new subpackages that need to be discovered

If you change dependencies in setup.py

If you rename/move major directories
