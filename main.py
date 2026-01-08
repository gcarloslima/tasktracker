from argparse import ArgumentParser

def main():
    parser = ArgumentParser(
        prog="task-cli", description="A command-line tool for managing tasks."
    )
    
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
