from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chrome_scripts.chrome_profiles import get_active_chrome_profile

def open_chrome_with_profile(website_url=None, config_Path=None, detach=True):
    active_profile = ''
    profile_directory = ''
    
    if (profile := get_active_chrome_profile(config_Path)):
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
