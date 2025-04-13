import pytest
from datetime import datetime, timedelta
from task import Task

def test_task_initialization():
    task = Task(
        project_id=1,
        title="Test Task",
        status="pending",
        description="This is a test task.",
        priority="medium",
        due_date=datetime.now() + timedelta(days=1),
    )
    assert task.project_id == 1
    assert task.title == "Test Task"
    assert task.status == "pending"
    assert task.description == "This is a test task."
    assert task.priority == "medium"
    assert task.due_date is not None
    assert isinstance(task.created_at, datetime)

def test_default_values():
    task = Task(
        project_id=2,
        title="Default Values Task",
    )
    assert task.status == "pending"
    assert task.priority == "medium"
    assert isinstance(task.created_at, datetime)

def test_title_length_validation():
    with pytest.raises(ValueError, match="Title must be between 1 and 100 characters."):
        Task(project_id=3, title="")

    with pytest.raises(ValueError, match="Title must be between 1 and 100 characters."):
        Task(project_id=3, title="T" * 101)

def test_status_validation():
    task = Task(project_id=4, title="Status Test", status="completed")
    assert task.status == "completed"

    with pytest.raises(ValueError, match="Status must be one of"):
        Task(project_id=4, title="Invalid Status Test", status="unknown")

def test_priority_validation():
    task = Task(project_id=5, title="Priority Test", priority="high")
    assert task.priority == "high"

    with pytest.raises(ValueError, match="Priority must be one of"):
        Task(project_id=5, title="Invalid Priority Test", priority="urgent")

def test_due_date_validation():
    task = Task(project_id=6, title="Due Date Test", due_date=datetime.now() + timedelta(days=1))
    assert task.due_date is not None

    with pytest.raises(ValueError, match="Due date must be in the future."):
        Task(project_id=6, title="Past Due Date Test", due_date=datetime.now() - timedelta(days=1))

def test_description_length_validation():
    task = Task(
        project_id=7,
        title="Description Test",
        description="This is a valid description within 255 characters."
    )
    assert task.description == "This is a valid description within 255 characters."

    with pytest.raises(ValueError, match="Description must be 255 characters or fewer."):
        Task(
            project_id=7,
            title="Long Description Test",
            description="D" * 256
        )
