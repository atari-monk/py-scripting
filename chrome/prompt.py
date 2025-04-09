from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument(r"user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://chat.openai.com/")

wait = WebDriverWait(driver, 2000)
input_area = wait.until(EC.element_to_be_clickable((By.ID, "prompt-textarea")))

prompt = "Write a Python function that calculates the Fibonacci sequence."
input_area.send_keys(prompt)
input_area.send_keys(Keys.RETURN)

time.sleep(10*60)
driver.quit()
