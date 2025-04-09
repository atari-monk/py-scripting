import time
from chrome import initialize_chrome_with_profile
from chatgpt import send_prompt, save_response, save_last_code_block

print("Initializing Chrome with profile... (4 seconds delay)")

driver = initialize_chrome_with_profile("https://chat.openai.com/", detach=True)
time.sleep(4)

assumptions = "Dont use comments in code. Do not wrtie anything but code."
task = "Write a Python function that calculates the Fibonacci sequence."
prompt = f"{assumptions} {task}"

print("Sending Prompt... (5 seconds delay)")

print(prompt)
send_prompt(driver, prompt)
time.sleep(5)

print("Saving Response... (1 second delay)")

response = save_response(driver=driver)
print("Response:")
print(response)
time.sleep(1)

prompt = "Write a automatic unit test."
print("Sending Prompt... (10 seconds delay)")

print(prompt)
send_prompt(driver, prompt)
time.sleep(10)

print("Saving Response... (1 second delay)")

response2 = save_response(driver=driver)
print("Response 2:")
print(response2)
time.sleep(1)

#driver.quit()