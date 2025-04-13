import argparse
from datetime import datetime
from typing import Optional
from log_project.ProjectTask import ProjectTask
from log_project.task_crud import TaskCRUD

def add_task(
    project_id: int,
    title: str,
    status: str = 'pending',
    description: Optional[str] = None,
    priority: str = 'medium',
    due_date_str: Optional[str] = None
) -> ProjectTask:
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    task = ProjectTask(
        project_id=project_id,
        title=title,
        status=status,
        description=description,
        priority=priority,
        due_date=due_date,
        created_at=datetime.now()
    )

    try:
        created_task = TaskCRUD().add_item(task.to_dict())
        if not created_task:
            raise RuntimeError("Failed to create task.")
        return task
    except Exception as e:
        raise RuntimeError(f"Unexpected error during task creation: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Add a new task.")
    parser.add_argument('project_id', type=int, help='ID of the project')
    parser.add_argument('title', type=str, help='Title of the task')
    parser.add_argument('--status', type=str, default='pending',
                      help='Status of the task (default: pending)')
    parser.add_argument('--description', type=str, default=None,
                      help='Description of the task')
    parser.add_argument('--priority', type=str, default='medium',
                      help='Priority of the task (default: medium)')
    parser.add_argument('--due-date', dest='due_date', type=str, default=None,
                      help='Due date of the task (format: YYYY-MM-DD)')
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        task = add_task(
            project_id=args.project_id,
            title=args.title,
            status=args.status,
            description=args.description,
            priority=args.priority,
            due_date_str=args.due_date
        )
        print(f"Task '{task.title}' created successfully with ID '{task.id}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()