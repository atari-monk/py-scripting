import sys
print(sys.path)  # Should contain your project root
from importlib.util import find_spec
print(find_spec("py_scripting"))  # Should show location

try:
    from chatgpt_scripts.chatgpt_automation import initialize_chatgpt_session
    print("SUCCESS! Import worked")
except ImportError as e:
    print(f"FAILED: {e}")