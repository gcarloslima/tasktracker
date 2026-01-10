from tasktracker.parser import build_parser

def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    print(args)


if __name__ == "__main__":
    main()
