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
