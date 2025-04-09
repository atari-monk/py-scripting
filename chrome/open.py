from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chrome_profiles as cp

active_profile = ''
if (profile := cp.get_active_chrome_profile()):
    active_profile = profile['chromeProfilePath']
    print(f"Active Profile: {active_profile}")
else:
    print("No active Chrome profile found")

options = Options()
options.add_argument(active_profile)
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://chat.openai.com/")

time.sleep(60*10)
print("Page opened. You can now inspect the elements.")
