import time
from colorama import Fore, Style
from chrome_scripts.chrome_automation import open_chrome_with_profile
from chatgpt_scripts.chatgpt_automation import send_prompt
from shared_library.colorama_utils import color_print

def open_chatgpt_session(page: str, config_Path: str, detach: bool, delay_seconds: int) -> None:
    message = f"1) Initializing Chrome with profile... ({delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    driver = open_chrome_with_profile(page, config_Path, detach=detach)
    time.sleep(delay_seconds)
    return driver

def send_chatgpt_prompt(driver, prompt: str, delay_seconds: int) -> None:
    message = f"2) Sending Prompt... ({delay_seconds} seconds delay)\n"
    color_print(message, Fore.RED, style=Style.BRIGHT)
    print(prompt)
    send_prompt(driver, prompt)
    time.sleep(delay_seconds)