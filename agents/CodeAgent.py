from agents.TaskAgent import TaskAgent
from agents.ChatGPTAgent import ChatGPTAgent

class CodeAgent:
    def __init__(self):
        self.verbose = False     

if __name__ == "__main__":
    t = TaskAgent()
    t.get_task("46210739-c4e6-463f-844f-21a278df5533")
    prompt = t.generate_prompt()
    print(prompt)
    c = ChatGPTAgent()
    c.send_prompt(prompt)
    c.save_code("data/code/fibonacci.py")
    c.close()