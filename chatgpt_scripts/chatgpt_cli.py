import time
from chrome_scripts.chrome_automation import open_chrome_with_profile

def initialize_chatgpt_session(page: str, config_Path: str, detach: bool, delay_seconds: int) -> None:
    print(f"1) Initializing Chrome with profile... ({delay_seconds} seconds delay)\n")
    driver = open_chrome_with_profile(page, config_Path, detach=detach)
    time.sleep(delay_seconds)
    return driver