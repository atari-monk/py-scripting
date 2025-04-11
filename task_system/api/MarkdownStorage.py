from pathlib import Path
from typing import Dict, Optional
from task_system.api.models import CodingTask

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

        task_path = self._get_task_path(task_id)
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