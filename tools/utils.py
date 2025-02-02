from datetime import datetime
from enum import Enum
from pathlib import Path
from sys import exit

from rcon.source import Client
from rich.console import Console
from rich.prompt import Prompt
from rich.status import Status

from .environment import Environment, Properties


def create_eula_file(eula: bool) -> None:
    file = Path("/server/eula.txt")
    file.touch()
    file.write_text(
        "\n".join(
            [
                "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).",
                f"#{datetime.now().isoformat()}",
                f"eula={str(eula).lower()}",
                "",  # Empty line, end of file
            ]
        )
    )

    if not eula:
        print("You need to agree to the EULA in order to run the server.")
        exit(1)


def create_server_properties_file(properties: Properties) -> None:
    properties_list: list[str] = []
    for key, value in properties.model_dump(by_alias=True).items():
        if isinstance(value, bool):
            _value = str(value).lower()
        elif isinstance(value, Enum):
            _value = value.value
        else:
            _value = value

        properties_list.append(f"{key}={_value}")

    extra_file = Path("/server/extra.properties")
    if extra_file.exists():
        properties_list.extend(["#Extra properties", extra_file.read_text().strip()])

    file = Path("/server/server.properties")
    file.touch()
    file.write_text(
        "\n".join(
            [
                "#Minecraft server properties",
                f"#{datetime.now().isoformat()}",
                *properties_list,
                "",  # Empty line, end of file
            ]
        )
    )


def rcon_connect(environment: Environment, console: Console, status: Status):
    with Client(
        host=environment.rcon_host,
        port=environment.server_properties.rcon_port,
        passwd=environment.server_properties.rcon_password,
        timeout=environment.rcon_timeout,
    ) as client:
        status.stop()
        console.log("Connected")

        command: str = ""
        while True:
            command = "/" + Prompt.ask("/")
            console.log(command)

            if command == "/exit":
                console.log("Closing the connection to the server", style="bold")
                break

            with console.status("Sending..."):
                response = client.run(*command.split(" "))
                console.log(response)

            if command == "/stop":
                console.log("Server stopped, closing connection", style="bold")
                break
