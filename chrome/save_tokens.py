from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

options = Options()
options.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://chat.openai.com/")

wait = WebDriverWait(driver, 60)
input_area = wait.until(EC.element_to_be_clickable((By.ID, "prompt-textarea")))

prompt = "Write a Python function that calculates the Fibonacci sequence."
input_area.send_keys(prompt)
input_area.send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='copy-turn-action-button']"))).click()

time.sleep(2)
copied_text = pyperclip.paste()

with open("response.md", "w", encoding="utf-8") as file:
    file.write(copied_text)

driver.quit()
