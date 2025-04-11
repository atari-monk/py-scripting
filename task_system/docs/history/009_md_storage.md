That's a great approach! Let's refactor the code to have separate storage classes and make the Markdown storage optional based on folder configuration. Here's how we can implement this:

1. First, let's update the models to include storage configuration:

```python
# File: models.py
from pydantic import BaseModel, Field, RootModel, field_validator
from typing import List, Optional, Dict
from datetime import datetime
import uuid

class TaskInputOutput(BaseModel):
    description: str
    examples: Optional[List[str]] = Field(default_factory=list)

class StorageConfig(BaseModel):
    md_folder: Optional[str] = None  # None means MD storage is disabled
    md_filename: Optional[str] = "task.md"  # Default filename

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
    storage_config: StorageConfig = Field(default_factory=StorageConfig)

    @field_validator('requirements')
    @classmethod
    def validate_requirements(cls, v):
        if len(v) < 1:
            raise ValueError("At least one requirement is needed")
        return v

class TaskListResponse(RootModel):
    root: Dict[str, CodingTask]
```

2. Now let's create separate storage classes:

```python
# File: storage.py
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime
from .models import CodingTask
import uuid

class MemoryStorage:
    def __init__(self):
        self.db = {}

    def create(self, task: CodingTask) -> CodingTask:
        self.db[task.id] = task.model_dump()
        return task

    def read(self, task_id: str) -> Optional[dict]:
        return self.db.get(task_id)

    def update(self, task_id: str, task: CodingTask) -> Optional[CodingTask]:
        if task_id not in self.db:
            return None
        self.db[task_id] = task.model_dump()
        return task

    def list_all(self) -> Dict[str, dict]:
        return self.db.copy()

class MarkdownStorage:
    def __init__(self):
        self.enabled = False

    def configure(self, md_folder: Optional[str], md_filename: str = "task.md"):
        self.enabled = md_folder is not None
        self.md_folder = Path(md_folder) if md_folder else None
        self.md_filename = md_filename

        if self.enabled:
            self.md_folder.mkdir(parents=True, exist_ok=True)

    def _get_task_path(self, task_id: str) -> Path:
        return self.md_folder / f"{task_id}_{self.md_filename}"

    def _task_to_md(self, task: CodingTask) -> str:
        """Convert a task to markdown format"""
        md = f"""# {task.title} (ID: {task.id})

**Description**: {task.description}

**Language**: {task.language}

**Difficulty**: {task.difficulty}

**Created at**: {task.created_at.isoformat()}
**Updated at**: {task.updated_at.isoformat()}

## Requirements:
"""
        for req in task.requirements:
            md += f"- {req}\n"

        if task.input:
            md += f"\n## Input:\n{task.input.description}\n"
            if task.input.examples:
                md += "\nExamples:\n"
                for ex in task.input.examples:
                    md += f"- {ex}\n"

        if task.output:
            md += f"\n## Output:\n{task.output.description}\n"
            if task.output.examples:
                md += "\nExamples:\n"
                for ex in task.output.examples:
                    md += f"- {ex}\n"

        if task.tags:
            md += "\n## Tags:\n"
            for tag in task.tags:
                md += f"- {tag}\n"

        return md

    def create(self, task: CodingTask) -> Optional[CodingTask]:
        if not self.enabled:
            return None

        task_path = self._get_task_path(task.id)
        task_path.write_text(self._task_to_md(task))
        return task

    def read(self, task_id: str) -> Optional[dict]:
        if not self.enabled:
            return None

        task_path = self._get_task_path(task.id)
        if not task_path.exists():
            return None

        # Note: This is just for demonstration
        # Full implementation would need to parse the MD back to a task
        return {"id": task_id, "source": "markdown"}

    def update(self, task_id: str, task: CodingTask) -> Optional[CodingTask]:
        if not self.enabled:
            return None

        task_path = self._get_task_path(task.id)
        if not task_path.exists():
            return None

        task_path.write_text(self._task_to_md(task))
        return task

    def list_all(self) -> Dict[str, dict]:
        if not self.enabled:
            return {}

        tasks = {}
        for file in self.md_folder.glob(f"*_{self.md_filename}"):
            task_id = file.name.split("_")[0]
            tasks[task_id] = {"id": task_id, "source": "markdown"}
        return tasks

class TaskStorage:
    def __init__(self):
        self.memory = MemoryStorage()
        self.markdown = MarkdownStorage()

    def configure_markdown(self, md_folder: Optional[str], md_filename: str = "task.md"):
        self.markdown.configure(md_folder, md_filename)

    def create(self, task: CodingTask) -> CodingTask:
        # Store in memory
        memory_task = self.memory.create(task)

        # Store in markdown if configured
        if task.storage_config.md_folder:
            self.markdown.configure(
                task.storage_config.md_folder,
                task.storage_config.md_filename
            )
            self.markdown.create(task)

        return memory_task

    def read(self, task_id: str) -> Optional[dict]:
        # Try memory first
        task = self.memory.read(task_id)
        if task:
            return task

        # Fall back to markdown if enabled
        if self.markdown.enabled:
            return self.markdown.read(task_id)

        return None

    def update(self, task_id: str, task: CodingTask) -> Optional[CodingTask]:
        # Update memory
        updated = self.memory.update(task_id, task)
        if not updated:
            return None

        # Update markdown if enabled
        if task.storage_config.md_folder:
            self.markdown.configure(
                task.storage_config.md_folder,
                task.storage_config.md_filename
            )
            self.markdown.update(task_id, task)

        return updated

    def list_all(self) -> Dict[str, dict]:
        # Get all from memory
        tasks = self.memory.list_all()

        # Merge with markdown if enabled
        if self.markdown.enabled:
            md_tasks = self.markdown.list_all()
            for task_id, task_data in md_tasks.items():
                if task_id not in tasks:
                    tasks[task_id] = task_data

        return tasks
```

3. Finally, update the main.py to use the new storage system:

```python
# File: main.py
from fastapi import FastAPI, HTTPException
from datetime import datetime
from task_system.api.models import CodingTask, TaskListResponse, StorageConfig
from task_system.api.storage import TaskStorage

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
```

Key improvements:

1. **Separate Storage Classes**: Now we have `MemoryStorage` and `MarkdownStorage` as independent classes
2. **Optional MD Storage**: MD storage is only used when `md_folder` is specified in the task's `storage_config`
3. **Per-Task Configuration**: Each task can specify where it should be stored in MD format
4. **Better Organization**: MD files are stored with task ID prefixes for easy identification
5. **Flexible Configuration**: You can configure the storage system globally or per-task

Example usage:

```python
# Task with MD storage
task_with_md = CodingTask(
    title="MD Task",
    description="This will be stored in MD",
    requirements=["req1"],
    language="python",
    storage_config=StorageConfig(md_folder="tasks_md")
)

# Task without MD storage
task_no_md = CodingTask(
    title="Memory Task",
    description="This will only be in memory",
    requirements=["req1"],
    language="python"
)
```

The MD files will be stored in the specified folder with names like `{task_id}_task.md`. This approach gives you maximum flexibility while keeping the code organized and maintainable.
