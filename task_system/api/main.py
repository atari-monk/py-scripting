from fastapi import FastAPI, HTTPException
from datetime import datetime
from task_system.api.models import CodingTask, TaskListResponse

app = FastAPI()

tasks_db = {}

@app.post("/tasks/", response_model=CodingTask)
async def create_task(task: CodingTask):
    tasks_db[task.id] = task.model_dump()
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
    tasks_db[task_id] = task.model_dump()
    return task

@app.get("/tasks/", response_model=TaskListResponse)
async def list_tasks():
    """List all tasks"""
    return tasks_db
