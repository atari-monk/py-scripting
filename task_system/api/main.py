from fastapi import FastAPI, HTTPException
from task_system.api.models import CodingTask, TaskListResponse
from task_system.api.TaskStorage import TaskStorage

app = FastAPI()
task_storage = TaskStorage()

@app.post("/tasks/", response_model=CodingTask)
async def create_task(task: CodingTask):
    stored_task = task_storage.create(task)
    return stored_task

@app.get("/tasks/{task_id}", response_model=CodingTask)
async def read_task(task_id: str):
    task = task_storage.read(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=CodingTask)
async def update_task(task_id: str, task: CodingTask):
    updated_task = task_storage.update(task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.get("/tasks/", response_model=TaskListResponse)
async def list_tasks():
    return task_storage.list_all()
