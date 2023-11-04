from rcon.source import Client
from argparse import ArgumentParser, MetavarTypeHelpFormatter
from getpass import getpass

CHAR_LENGTH = 64
TITLE = "Remote Console"
VERSION = "1.0.0"


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="RemoteConsole",
        description="Remote console connecting via RCON protocol.",
        formatter_class=MetavarTypeHelpFormatter,
    )
    parser.add_argument(
        "--host",
        help="hostname to RCON server",
        type=str,
    )
    parser.add_argument(
        "--port",
        help="port to RCON server",
        type=int,
    )
    parser.add_argument(
        "--password",
        help="password to RCON server",
        type=str,
    )

    return parser


def get_rcon_info(parser: ArgumentParser) -> tuple[str, int, str]:
    args = parser.parse_args()

    print_title()

    if args.host or args.port or args.password:
        print(
            f"Host: {args.host}",
            f"Port: {args.port}",
            "Password: ",
            sep="\n",
        )
        return (args.host, args.port, args.password)

    host = input("Host: ")
    port = input("Port: ")
    password = getpass("Password: ")

    return (host, int(port), password)


def print_title() -> None:
    spacing = CHAR_LENGTH - len(VERSION) - 1

    print("=" * CHAR_LENGTH)
    print(TITLE.ljust(spacing), VERSION)
    print("=" * CHAR_LENGTH)


def rcon_connect(host: str, port: int, password: str) -> None:
    with Client(host=host, port=port, passwd=password) as client:
        while True:
            command = input("> ")

            if command == "exit":
                break

            response = client.run(command)
            print(response)

            if command == "stop":
                break


def main() -> None:
    parser = get_parser()
    host, port, password = get_rcon_info(parser)
    print("-" * CHAR_LENGTH)
    print("Type `exit` to close the connection.\n")
    rcon_connect(host, port, password)


if __name__ == "__main__":
    main()
