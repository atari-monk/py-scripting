from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

def send_prompt(driver, prompt, input_area_id="prompt-textarea"):
    try:
        input_area = driver.find_element(By.ID, input_area_id)
        input_area.clear()
        input_area.send_keys(prompt)
        input_area.send_keys(Keys.RETURN)
        print("Prompt sent successfully")
        return True
    except Exception as e:
        print(f"Failed to send prompt: {str(e)}")
        return False
    
def save_response(driver, output_file="response.md", wait_time=60):
    try:
        last_copy_button_xpath = "(//button[contains(., 'Kopiuj') or @data-testid='copy-turn-action-button'])[last()]"
        copy_button = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, last_copy_button_xpath)))
        driver.execute_script("arguments[0].click();", copy_button)
        time.sleep(1)
        response = pyperclip.paste()
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(response + "\n\n")
        return response
    except Exception as e:
        print(f"Error saving response: {e}")
        return None
    
def save_last_code_block(driver, output_file="response.md", wait_time=60):
    try:
        copy_button_xpath = "(//button[contains(., 'Kopiuj')])[last()]"
        copy_button = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, copy_button_xpath)))
        driver.execute_script("arguments[0].click();", copy_button)
        time.sleep(1)
        response = pyperclip.paste()
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(response + "\n\n")
        return response
    except Exception as e:
        print(f"Error saving last code block: {e}")
        return None