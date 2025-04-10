from chatgpt_scripts.chatgpt_cli import open_chatgpt_session, save_chatgpt_code_block, send_chatgpt_prompt

driver = open_chatgpt_session(
    page="https://chat.openai.com/",
    config_Path="data/chrome_profiles.json",
    detach=True,
    delay_seconds=4
)

assumptions = "Dont use comments in code. Do not wrtie anything but code."
task = "Write a Python function that calculates the Fibonacci sequence."

send_chatgpt_prompt(driver=driver, prompt=f"{assumptions} {task}", delay_seconds=5)

save_chatgpt_code_block(driver=driver, delay_seconds=1)

send_chatgpt_prompt(driver=driver, prompt="Write a automatic unit test.", delay_seconds=10)

save_chatgpt_code_block(driver=driver, delay_seconds=1)

driver.quit()