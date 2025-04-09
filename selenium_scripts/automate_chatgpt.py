import time
from chrome import initialize_chrome_with_profile
from chatgpt import send_prompt, save_response, save_last_code_block

delay = 4
print(f"1) Initializing Chrome with profile... ({delay} seconds delay)\n")

driver = initialize_chrome_with_profile("https://chat.openai.com/", detach=True)
time.sleep(delay)

assumptions = "Dont use comments in code. Do not wrtie anything but code."
task = "Write a Python function that calculates the Fibonacci sequence."
prompt = f"{assumptions} {task}"

delay = 5
print(f"2) Sending Prompt... ({delay} seconds delay)\n")

print(prompt)
send_prompt(driver, prompt)
time.sleep(delay)

delay = 1
print(f"3) Saving Response... ({delay} second delay)\n")

response = save_last_code_block(driver=driver)
print("Response 1:")
print(response)
time.sleep(delay)

delay = 10
prompt = "Write a automatic unit test."
print(f"4) Sending Prompt... ({delay} seconds delay)")

print(prompt)
send_prompt(driver, prompt)
time.sleep(10)

delay = 1
print(f"5) Saving Response... ({delay} second delay)")

response2 = save_last_code_block(driver=driver)
time.sleep(1)

print("Response 2:")
print(response2)

#driver.quit()