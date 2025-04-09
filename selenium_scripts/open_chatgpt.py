import helpers as h

driver = h.initialize_chrome_with_profile("https://chat.openai.com/", detach=False)

assumptions = "Dont use comments in code. Do not wrtie anything but code."

h.save_chatgpt_prompt_response(
    driver=driver, 
    prompt=f"Write a Python function that calculates the Fibonacci sequence. {assumptions}", 
    output_file="fibonacci_response.md",
    input_area_id="prompt-textarea",
    copy_button_xpath="//button[@data-testid='copy-turn-action-button']",
    response_indicator_xpath="//div[contains(@class, 'markdown')]",
    close_driver=False)

h.save_chatgpt_prompt_response(
    driver=driver, 
    prompt="Write a Python function that calculates the Fibonacci sequence. Write automatic unit test for it. Dont use comments in code. Do not wrtie anything but code.", 
    output_file="fibonacci_response.md",
    input_area_id="prompt-textarea",
    copy_button_xpath="//button[@data-testid='copy-turn-action-button']",
    response_indicator_xpath="//div[contains(@class, 'markdown')]",
    close_driver=True)