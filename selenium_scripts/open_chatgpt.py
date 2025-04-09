import helpers as h

driver = h.initialize_chrome_with_profile("https://chat.openai.com/", detach=False)

assumptions = "Dont use comments in code. Do not wrtie anything but code."
tasks = ["Write a Python function that calculates the Fibonacci sequence.", "Write automatic unit test for:"]
fileName = "Fibonacci_Response.md"

prompt1 = f"""{assumptions} 
{tasks[0]}"""

print(f"""Prompt1: 
{prompt1}\n""")

response1 = h.save_chatgpt_prompt_response(
    driver=driver, 
    prompt=prompt1, 
    output_file=fileName)

print(f"""Response1: 
{response1}\n""")

prompt2 = f"""{assumptions} 
{tasks[1]} 
{response1}"""

print(f"""Prompt2: 
{prompt2}\n""")

response2 = h.save_chatgpt_prompt_response(
    driver=driver, 
    prompt=prompt2, 
    output_file=fileName)

print(f"""Response2: 
{response2}\n""")

driver.quit()
