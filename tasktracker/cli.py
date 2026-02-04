from tasktracker.parser import build_parser
from tasktracker.action_handler import handle_action

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    handle_action(args.command, args.title)

if __name__ == "__main__":
    main()
