You're right! We need to add a `GET /tasks/` endpoint to list all tasks in the FastAPI backend. Here's how to fix both the API and CLI:

## 1. First, update your FastAPI backend (`task_system/api/main.py`):

```python
# Add this endpoint to your existing FastAPI code
@app.get("/tasks/", response_model=dict[str, dict])
async def list_tasks():
    """List all tasks"""
    return tasks_db  # Returns the entire in-memory database
```

## 2. Then update the CLI's `list_tasks()` function:

```python
def list_tasks():
    print("\n=== Task List ===")
    response = requests.get(f"{API_BASE_URL}/tasks/")

    if response.ok:
        tasks = response.json()
        if not tasks:
            print("No tasks found")
            return

        # Display as a numbered list
        for i, (task_id, task) in enumerate(tasks.items(), 1):
            print(f"{i}. {task['title']} (ID: {task_id})")
            print(f"   Language: {task.get('language', 'N/A')}")
            print(f"   Difficulty: {task.get('difficulty', 'N/A')}")
            print("-" * 40)

        # Add option to view details
        task_ids = list(tasks.keys())
        choices = [
            questionary.Choice(f"View details of task {i+1}", value=task_ids[i])
            for i in range(len(task_ids))
        ] + [questionary.Choice("Return to main menu", value=None)]

        selected = questionary.select(
            "Select a task to view details or return:",
            choices=choices
        ).ask()

        if selected:
            view_task(selected)
    else:
        handle_response(response)
```

## 3. Update your API model to include the response model:

```python
from typing import Dict  # Add to imports

# Add this after your existing models
class TaskListResponse(BaseModel):
    __root__: Dict[str, CodingTask]  # Maps task IDs to task objects

# Then update your list endpoint decorator:
@app.get("/tasks/", response_model=TaskListResponse)
```

## Testing the Changes:

1. First restart your FastAPI server:

```bash
uvicorn task_system.api.main:app --reload
```

2. Then run the CLI:

```bash
python -m task_system.cli.task_wizard
```

3. Now when you select "List all tasks":

- It will show all tasks in a clean format
- Let you select any task to view its full details
- Handle empty states gracefully

## Error Handling Improvements:

The CLI will now properly handle:

- No tasks existing (shows "No tasks found")
- API connection errors
- Malformed responses
- Provides clear navigation back to the menu

Would you like me to add any additional features to the task listing, such as:

- Filtering by language/difficulty
- Pagination support
- Sorting options
- Export to CSV/JSON?
