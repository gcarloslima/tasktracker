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
    createdAt: datetime
    updatedAt: datetime
    status: Status = Status.TODO
