import sys
from importlib.util import find_spec

print(sys.path)
print(find_spec("py_scripting"))

try:
    from chatgpt_scripts.chatgpt_automation import initialize_chatgpt_session
    print("SUCCESS! Import worked")
except ImportError as e:
    print(f"FAILED: {e}")