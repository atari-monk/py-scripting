pip uninstall py_scripting -y
Remove-Item -Path "C:\atari-monk\code\py-scripting\py_scripting.egg-info" -Recurse -Force
pip install -e .
