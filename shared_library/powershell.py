import subprocess
import os

def run_powershell_script(script_path):
    script_path = os.path.abspath(script_path)
    command = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            if len(result.stdout) > 0:
                print("Script output:")
                print(result.stdout)
        else:
            print("Error occurred:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    script_path = r"C:\atari-monk\code\py-scripting\ps1_scripts\text_to_speech.ps1"
    run_powershell_script(script_path)