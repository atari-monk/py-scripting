from chatgpt_scripts.chatgpt_cli import open_chatgpt_session, save_chatgpt_code_block, send_chatgpt_prompt

class ChatGPTAgent:
    def __init__(self):
        self.driver = None
        self.open()
    
    def open(self):
      if self.driver is not None:
        self.driver.quit()
      self.driver = open_chatgpt_session(
        page="https://chat.openai.com/",
        config_Path="data/chrome_profiles.json",
        detach=True,
        delay_seconds=5
      )
    
    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def send_prompt(self, prompt, delay_seconds=5):
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        send_chatgpt_prompt(driver=self.driver, prompt=prompt, delay_seconds=delay_seconds)

    def save_code(self, output_file_path:str, delay_seconds=1):
        if self.driver is None:
            raise Exception("ChatGPT session is not open.")
        save_chatgpt_code_block(driver=self.driver, output_file_path=output_file_path, delay_seconds=delay_seconds)
  
if __name__ == "__main__":
    agentChatGPT = ChatGPTAgent()
    agentChatGPT.send_prompt("Dont use comments in code. Do not wrtie anything but code. Write a Python function that calculates the Fibonacci sequence.")
    agentChatGPT.save_code("data/code/fibonacci.py")
    agentChatGPT.send_prompt("Write a automatic unit test.")
    agentChatGPT.save_code("data/code/fibonacci.test.py")
    agentChatGPT.close()