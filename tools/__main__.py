import argparse
from sys import exit

from rich.console import Console

from .environment import Environment
from .utils import create_eula_file, create_server_properties_file, rcon_connect

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--console", help="Run RCON console", action="store_true")
    parser.add_argument("--server", help="Run server", action="store_true")

    arguments = parser.parse_args()
    if not any(arguments.__dict__.values()):
        parser.print_help()
        exit(1)

    environment = Environment()

    if arguments.server:
        create_eula_file(environment.eula)
        create_server_properties_file(environment.server_properties)
        exit(0)

    if arguments.console:
        console = Console(width=64, log_path=False)

        console.print("=" * 64, style="bright_black bold")
        console.print("RCON Console")
        console.print("=" * 64, style="bright_black bold")

        status = console.status("Connecting...")

        try:
            status.start()
            rcon_connect(environment, console, status)
        except ConnectionRefusedError:
            console.log("Connection timeout", style="red bold")
            exit(1)
        finally:
            status.stop()
