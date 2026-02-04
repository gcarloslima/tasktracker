from argparse import ArgumentParser

from tasktracker.schema import Status


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="task-cli", description="A command-line tool for managing tasks."
    )

    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument(
        "title"
    )
    
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "status",
        nargs="?",
        type=Status,
        choices=list(Status),
    )


    return parser

