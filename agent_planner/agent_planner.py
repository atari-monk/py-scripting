from chatgpt_scripts.chatgpt_cli import open_chatgpt_session

driver = open_chatgpt_session(
    page="https://chat.openai.com/",
    config_Path="../data/chrome_profiles.json",
    detach=True,
    delay_seconds=4
)