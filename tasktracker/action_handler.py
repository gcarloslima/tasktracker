from argparse import Namespace
from tasktracker.schema import Command, Status, Task
from datetime import datetime
import json
import os
from pathlib import Path


def handle_action(args: Namespace) -> None:
    match args.command:
        case Command.ADD:
            _add(args.title)
        case Command.LIST:
            _list(args.status)
        case Command.UPDATE:
            _update(args.id, args.new_title)
        case Command.DELETE:
            _delete(args.id)
        case Command.MARK_IN_PROGRESS:
            _mark_in_progress(args.id)
        case Command.MARK_DONE:
            raise NotImplementedError()


def _get_file_path() -> Path:
    file_path_name = os.environ.get("STORAGE_FILE_PATH", "storage/data.json")
    return Path(file_path_name)


def _load_file() -> dict:
    path = _get_file_path()

    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    return {"tasks": []}


def _save_file(data: dict) -> None:
    path = _get_file_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
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
        updated_at=now,
    )

    tasks.append(new_task.to_dict())
    _save_file(data)
    print(f"Task added successfully: (ID: {new_task.id})")


def _list(status: Status | None) -> None:
    data = _load_file()
    if status:
        tasks = [t for t in data["tasks"] if t["status"] == status]
    else:
        tasks = data["tasks"]

    for task in tasks:
        print("-" * 50)
        print(f"Task #{task['id']}")
        print(f"Name: {task['description']}")
        print(f"Status: {task['status']}")
        print("-" * 50)


def _update(id: int, new_title: str) -> None:
    data = _load_file()
    task = next((t for t in data["tasks"] if t["id"] == id), None)
    if task:
        task["description"] = new_title
        _save_file(data)

        print("Task updated with success")


def _delete(id: int) -> None:
    data = _load_file()
    tasks = data["tasks"]

    for i, t in enumerate(tasks):
        if t.get("id") == id:
            tasks.pop(i)
            _save_file(data)
            print("Task deleted with success")
            return

    print(f"No task with ID: {id} was found")


def _mark_in_progress(id: int) -> None:
    data = _load_file()
    tasks = data["tasks"]

    task = next((t for t in tasks if t["id"] == id), None)

    if task:
        task["status"] = Status.IN_PROGRESS
        _save_file(data)
        print("Task status updated with success")
