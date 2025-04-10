import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chrome_profiles as cp

def initialize_chrome_with_profile(website_url=None, detach=True):
    active_profile = ''
    profile_directory = ''
    
    if (profile := cp.get_active_chrome_profile()):
        active_profile = profile['chromeProfilePath']
        profile_directory = profile['profileDirectory']
        print(f"Active Profile: {active_profile}, Profile Directory: {profile_directory}")
    else:
        print("No active Chrome profile found")
        return None
    
    options = Options()
    options.add_argument(fr"user-data-dir={active_profile}")
    options.add_argument(f"profile-directory={profile_directory}")
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    if detach:
        options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    
    if website_url:
        driver.get(website_url)
        print(f"Page opened at {website_url}. You can now inspect the elements.")
    else:
        print("Chrome initialized with profile but no page opened (no URL provided).")
    
    return driver

def initialize_chatgpt_session(page: str, detach: bool, delay_seconds: int) -> None:
    print(f"1) Initializing Chrome with profile... ({delay_seconds} seconds delay)\n")
    driver = initialize_chrome_with_profile(page, detach=detach)
    time.sleep(delay_seconds)
    return driver