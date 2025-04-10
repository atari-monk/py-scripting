from selenium_scripts.chatgpt import initialize_chatgpt_session

driver = initialize_chatgpt_session(
    page="https://chat.openai.com/",
    config_Path="../data/chrome_profiles.json",
    detach=True,
    delay_seconds=4
)