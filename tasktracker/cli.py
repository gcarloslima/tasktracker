from argparse import ArgumentParser


def _build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="task-cli", description="A command-line tool for managing tasks."
    )

    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    return parser


def main(argv=None):
    parser = _build_parser()
    args = parser.parse_args(argv)
    print(args)


if __name__ == "__main__":
    main()
