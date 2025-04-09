import time
from chrome import initialize_chrome_with_profile
from chatgpt import send_prompt, save_response

assumptions = "Dont use comments in code. Do not wrtie anything but code."
task = "Write a Python function that calculates the Fibonacci sequence."
prompt = f"{assumptions} {task}"

print("Initializing Chrome with profile...")
driver = initialize_chrome_with_profile("https://chat.openai.com/", detach=True)

time.sleep(4)

print("Sending Prompt...")
print(prompt)
send_prompt(driver, prompt)

time.sleep(5)

print("Saving Response...")
response = save_response(driver=driver)

print("Response:")
print(response)

#driver.quit()