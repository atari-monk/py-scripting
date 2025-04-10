# Pydantic V2 Migration Guide for Your Code

You're seeing a deprecation warning because you're using Pydantic V1 style validators (`@validator`) in your code. Here's how to update your code to use Pydantic V2's `@field_validator`:

## Updated Code

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator  # Changed import
from typing import List, Optional
from datetime import datetime
import uuid

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

    @field_validator('requirements')  # Changed decorator
    @classmethod  # Added classmethod decorator
    def validate_requirements(cls, v):  # Method remains the same
        if len(v) < 1:
            raise ValueError("At least one requirement is needed")
        return v

@app.post("/tasks/", response_model=CodingTask)
async def create_task(task: CodingTask):
    tasks_db[task.id] = task.model_dump()  # Changed from .dict() to .model_dump()
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
    tasks_db[task_id] = task.model_dump()  # Changed from .dict() to .model_dump()
    return task
```

## Key Changes Made:

1. **Validator Import**: Changed from `validator` to `field_validator`
2. **Decorator**: Changed `@validator` to `@field_validator`
3. **Class Method**: Added `@classmethod` decorator (required in Pydantic V2)
4. **Serialization**: Changed `.dict()` to `.model_dump()` (Pydantic V2's method)

## Additional Recommendations:

1. Consider using `datetime.now(timezone.utc)` instead of `datetime.utcnow()` as `utcnow()` is also deprecated
2. You might want to add more field validators for other fields (like checking language is valid, difficulty is one of expected values, etc.)
3. Consider using Pydantic's `Config` class to add more model-wide configurations if needed

The functionality remains exactly the same, but now your code is future-proofed for Pydantic V2.
