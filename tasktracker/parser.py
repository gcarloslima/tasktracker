from argparse import ArgumentParser

from tasktracker.schema import Status


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="task-cli", description="A command-line tool for managing tasks."
    )

    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument(
        "title",
        type=str
    )
    
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "status",
        nargs="?",
        type=Status,
        choices=list(Status),
    )

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("new_title", type=str)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    return parser

