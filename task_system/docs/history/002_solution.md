Here's a comprehensive solution for your Idea Agent Coder task system:

## Enhanced Task Model (JSON Schema)

```json
{
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "CodingTask",
	"description": "A task definition for coder agents",
	"type": "object",
	"properties": {
		"id": {
			"type": "string",
			"description": "Unique identifier for the task",
			"pattern": "^[a-z0-9_]+$"
		},
		"title": {
			"type": "string",
			"description": "Brief descriptive title",
			"minLength": 5,
			"maxLength": 100
		},
		"description": {
			"type": "string",
			"description": "Detailed task description",
			"minLength": 20
		},
		"requirements": {
			"type": "array",
			"items": {
				"type": "string",
				"minLength": 5
			},
			"minItems": 1
		},
		"input": {
			"type": "object",
			"properties": {
				"description": { "type": "string" },
				"examples": {
					"type": "array",
					"items": { "type": "string" }
				}
			},
			"required": ["description"]
		},
		"output": {
			"type": "object",
			"properties": {
				"description": { "type": "string" },
				"examples": {
					"type": "array",
					"items": { "type": "string" }
				}
			},
			"required": ["description"]
		},
		"language": {
			"type": "string",
			"enum": ["python", "javascript", "java", "c++", "go", "rust", "other"]
		},
		"difficulty": {
			"type": "string",
			"enum": ["easy", "medium", "hard"]
		},
		"tags": {
			"type": "array",
			"items": { "type": "string" },
			"uniqueItems": true
		},
		"created_at": { "type": "string", "format": "date-time" },
		"updated_at": { "type": "string", "format": "date-time" }
	},
	"required": ["id", "title", "description", "requirements", "language"],
	"additionalProperties": false
}
```

Example:

```json
{
	"id": "task_42",
	"title": "Reverse a string",
	"description": "Write a function that reverses the given input string.",
	"requirements": ["The function must handle Unicode characters"],
	"input": {
		"description": "A string to be reversed",
		"examples": ["hello", "世界"]
	},
	"output": {
		"description": "The reversed string",
		"examples": ["olleh", "界世"]
	},
	"language": "python",
	"difficulty": "easy",
	"tags": ["string", "algorithm"]
}
```

## FastAPI Implementation

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator, Field
from typing import List, Optional
from datetime import datetime
import uuid
import json

app = FastAPI()

# In-memory storage (replace with database in production)
tasks_db = {}

class TaskInputOutput(BaseModel):
    description: str
    examples: Optional[List[str]] = Field(default_factory=list)

class CodingTask(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    requirements: List[str]
    input: Optional[TaskInputOutput] = None
    output: Optional[TaskInputOutput] = None
    language: str
    difficulty: Optional[str] = "medium"
    tags: Optional[List[str]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('requirements')
    def validate_requirements(cls, v):
        if len(v) < 1:
            raise ValueError("At least one requirement is needed")
        return v

@app.post("/tasks/", response_model=CodingTask)
async def create_task(task: CodingTask):
    tasks_db[task.id] = task.dict()
    return task

@app.get("/tasks/{task_id}", response_model=CodingTask)
async def read_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=CodingTask)
async def update_task(task_id: str, task: CodingTask):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task.updated_at = datetime.utcnow()
    tasks_db[task_id] = task.dict()
    return task
```

## CLI Interface

```python
import questionary
from typing import Optional, List
import requests
import json

API_BASE_URL = "http://localhost:8000"

def prompt_task_creation():
    # Mandatory fields
    task_data = {
        "title": questionary.text("Task title:").ask(),
        "description": questionary.text("Task description:").ask(),
        "requirements": prompt_list("Enter requirements (one per line, empty to finish):"),
        "language": questionary.select(
            "Programming language:",
            choices=["python", "javascript", "java", "c++", "go", "rust", "other"]
        ).ask(),
    }

    # Optional fields
    if questionary.confirm("Would you like to add input specifications?").ask():
        task_data["input"] = {
            "description": questionary.text("Input description:").ask(),
            "examples": prompt_list("Enter input examples (one per line, empty to finish):")
        }

    if questionary.confirm("Would you like to add output specifications?").ask():
        task_data["output"] = {
            "description": questionary.text("Output description:").ask(),
            "examples": prompt_list("Enter output examples (one per line, empty to finish):")
        }

    task_data["difficulty"] = questionary.select(
        "Difficulty level:",
        choices=["easy", "medium", "hard"],
        default="medium"
    ).ask()

    task_data["tags"] = prompt_list("Enter tags (comma separated):", comma_separated=True)

    return task_data

def prompt_list(prompt: str, comma_separated: bool = False) -> List[str]:
    if comma_separated:
        answer = questionary.text(prompt).ask()
        return [item.strip() for item in answer.split(",") if item.strip()]
    else:
        items = []
        while True:
            item = questionary.text(f"{prompt}").ask()
            if not item:
                break
            items.append(item)
        return items

def create_task_via_api(task_data):
    response = requests.post(f"{API_BASE_URL}/tasks/", json=task_data)
    if response.status_code == 200:
        print("Task created successfully!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error creating task: {response.text}")

if __name__ == "__main__":
    print("=== Task Creation Wizard ===")
    task_data = prompt_task_creation()
    create_task_via_api(task_data)
```

## Architecture Recommendation

1. **Three-Layer Architecture**:

   - CLI Interface (User Interaction)
   - API Layer (FastAPI)
   - Storage Layer (Start with in-memory, then move to database)

2. **Validation**:

   - Use Pydantic for data validation
   - JSON Schema for documentation and external validation

3. **Extensions**:

   - Add authentication for API endpoints
   - Implement task versioning
   - Add search functionality
   - Support for file attachments
   - Task templates for common patterns

4. **Agent Integration**:
   - The same API can be used by both human users and automated agents
   - Consider adding an "agent_mode" flag for machine-friendly responses

Would you like me to elaborate on any particular aspect of this solution?
