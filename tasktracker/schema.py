from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class Command(str, Enum):
    ADD = "add"
    LIST = "list"
    UPDATE = "update"
    DELETE = "delete"
    MARK_IN_PROGRESS = "mark-in-progress"
    MARK_DONE = "mark-done"


class Status(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    description: str
    created_at: datetime
    updated_at: datetime
    status: Status = Status.TODO

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat(),
            "status": self.status.value,
        }
