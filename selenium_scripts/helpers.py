from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chrome_profiles as cp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import pyperclip
import time

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

# Example usage:
# driver = initialize_chrome_with_profile()  # Opens Chrome with profile but no page
# driver = initialize_chrome_with_profile("https://www.google.com")  # Opens Google
# driver = initialize_chrome_with_profile(detach=False)  # Opens Chrome but closes when script ends

def save_chatgpt_prompt_response(
    driver, 
    prompt, 
    output_file="response.md", 
    wait_time=60,
    input_area_id="prompt-textarea",
    copy_button_xpath="//button[@data-testid='copy-turn-action-button']",
    response_indicator_xpath="//div[contains(@class, 'markdown')]",
    close_driver=False
):
    try:
        wait = WebDriverWait(driver, wait_time)
        
        print("Waiting for input area...")
        input_area = wait.until(EC.element_to_be_clickable((By.ID, input_area_id)))
        print("Found input area. Sending prompt...")
        input_area.clear()
        input_area.send_keys(prompt)
        input_area.send_keys(Keys.RETURN)
        
        print("Waiting for response...")
        wait.until(EC.presence_of_element_located((By.XPATH, response_indicator_xpath)))
        
        print("Waiting for response to be fully visible and non-empty...")
        response_element = wait.until(EC.visibility_of_element_located((By.XPATH, response_indicator_xpath)))
        
        response_text = response_element.text.strip()
        if not response_text:
            raise ValueError("Response is empty, likely failed to generate a proper response.")
        
        print("Response is ready to be copied.")
        
        print("Waiting for copy button...")
        copy_button = wait.until(EC.element_to_be_clickable((By.XPATH, copy_button_xpath)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", copy_button)
        time.sleep(0.5)
        
        print("Clicking copy button...")
        try:
            copy_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", copy_button)
        
        time.sleep(1)
        
        print("Retrieving copied text...")
        copied_text = pyperclip.paste()
        if not copied_text.strip():
            raise ValueError("Clipboard appears to be empty - possibly failed to copy response")
        
        print(f"Saving response to {output_file}...")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(copied_text)
            
        print(f"Successfully saved response to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        if close_driver:
            driver.quit()
        return False
    
    finally:
        if close_driver:
            driver.quit()
    
    return True

# Example usage:
# save_chatgpt_prompt_response(
#     driver=driver, 
#     prompt="Write a Python function that calculates the Fibonacci sequence.", 
#     output_file="fibonacci_response.md",
#     input_area_id="prompt-textarea",
#     copy_button_xpath="//button[@data-testid='copy-turn-action-button']",
#     close_driver=True  # Set to True if you want to close the driver
# )