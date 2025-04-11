from pydantic import BaseModel, Field, RootModel, field_validator
from typing import List, Optional
from datetime import datetime
from typing import Dict
import uuid

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

    @field_validator('requirements')
    @classmethod
    def validate_requirements(cls, v):
        if len(v) < 1:
            raise ValueError("At least one requirement is needed")
        return v

class TaskListResponse(RootModel):
    root: Dict[str, CodingTask]