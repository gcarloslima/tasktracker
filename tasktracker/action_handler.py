from tasktracker.schema import Command, Task
from datetime import datetime
import json
import os
from pathlib import Path


def handle_action(command: Command, argument: str) -> None:
    match(command):
        case Command.ADD:
            _add(argument)
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
        

def _get_file_path() -> Path:
    file_path_name = os.environ.get("STORAGE_FILE_PATH", "storage/data.json")
    return Path(file_path_name)

def _load_file() -> dict:
    path = _get_file_path()

    if path.exists():
        print(f"Loading data from {path}")
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
        
    return { "tasks": [] }


def _save_file(data: dict) -> None:
    path = _get_file_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path,"w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)


def _get_new_task_id(tasks: list):
    if tasks:
        return tasks[-1]["id"] + 1
    
    return 1


def _add(task_name: str) -> None:
    now = datetime.now()

    data = _load_file()
    tasks: list = data["tasks"]

    new_task = Task(
        id=_get_new_task_id(tasks),
        description=task_name,
        created_at=now,
        updated_at=now
    )
    

    tasks.append(new_task.to_dict())
    _save_file(data)
    print(f"Task added successfully: (ID: {new_task.id})")


