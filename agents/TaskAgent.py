import requests

class TaskAgent:
    def __init__(self):
        self.verbose = False     
        self.task = None
        self.API_BASE_URL = "http://localhost:8000"
    
    def get_task(self, task_id: str):
        response = requests.get(f"{self.API_BASE_URL}/tasks/{task_id}")
        if response.status_code == 200:
            self.task = response.json()
            print("Task fetched successfully.")
            if self.verbose:
                self.printTask()
        else:
            print("Error fetching task.")
            print(f"Status Code: {response.status_code}")
    
    def printTask(self):
        if self.task:
            print(f"Task ID: {self.task['id']}")
            print(f"Title: {self.task['title']}")
            print(f"Description: {self.task['description']}")
            print(f"Requirements: {', '.join(self.task['requirements'])}")
            print(f"Language: {self.task['language']}")
            print(f"Difficulty: {self.task['difficulty']}")
        else:
            print("No task loaded.")
    
    def generate_prompt(self) -> str:
        if not self.task:
            return "No task loaded. Please load a task first."
    
        prompt = f"""
Task Title: {self.task['title']}
Description: {self.task['description']}
Requirements:
"""
    
        for req in self.task['requirements']:
            prompt += f"- {req.strip()}\n"  # No extra indentation
    
        prompt += f"""
Additional Information:
- Language: {self.task['language']}
- Difficulty: {self.task['difficulty']}
"""
        return prompt

if __name__ == "__main__":
    t = TaskAgent()
    t.get_task("46210739-c4e6-463f-844f-21a278df5533")
    print(t.generate_prompt())
