from tasktracker.schema import Command, Task
from datetime import datetime
import json
import os


def handle_action(command: Command, argument: str) -> None:
    match(command):
        case Command.ADD:
            _add(argument)
            raise NotImplementedError()
        case Command.LIST:
            raise NotImplementedError()
        case Command.UPDATE:
            raise NotImplementedError()
        case Command.DELETE:
            raise NotImplementedError()
        case Command.MARK_IN_PROGRESS:
            raise NotImplementedError()
        case Command.MARK_DONE:
            raise NotImplementedError()
        

def _add(task_name: str) -> None:
    now = datetime.now()
    with open(os.environ.get("STORAGE_FILE_PATH", "storage/tasks.json"), "r") as f:
        data = json.load(f)
        tasks = data.tasks
        print(tasks)
        new_task = Task(
            id=1,
            description=task_name,
            createdAt=now,
            updatedAt=now
    
        )
        tasks.extend(new_task.__dict__)


