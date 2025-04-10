from ..selenium_scripts.chrome import initialize_chatgpt_session

driver = initialize_chatgpt_session(
    page="https://chat.openai.com/",
    detach=True,
    delay_seconds=4
)