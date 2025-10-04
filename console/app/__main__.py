from datetime import datetime

from rcon.source import Client  # type: ignore

from .spinner import Spinner
from .styled_string import Color, styled_string
from .utils import get_client_configuration, get_logger

if __name__ == "__main__":
    logger = get_logger()
    client_conf = get_client_configuration()

    logger.critical(datetime.now().isoformat())
    logger.debug("RCON server: %s:%s", client_conf["host"], client_conf["port"])
    print(styled_string("======== Console App ========", bold=True))

    loader = Spinner()
    loader.start("Connecting to server...")
    logger.info("Staring connection")
    try:
        with Client(**client_conf) as client:  # type: ignore
            logger.debug("Socket connected, confirming connection")
            client.run("/help")  # Confirm connection
            logger.debug("Connection ready")
            loader.stop()

            print(
                styled_string("Connected", Color.GREEN),
                styled_string("| Send /exit command to exit the app.", Color.BLACK),
            )

            while True:
                print(styled_string("\n⣿", Color.BLACK), end=" ")
                command = "/" + input("/\n\033[1A\033[3C").strip()
                logger.info("Sending command: '%s'", command)

                if command == "/exit":
                    logger.debug("Break loop")
                    break

                print("\033[1A", end="")  # Replace input line with loader
                loader.start(command)
                response = client.run(*command.split(" "))
                logger.debug("Received response: '%s'", response)
                loader.stop()

                print(styled_string(f"⡇{datetime.now().strftime('%H:%M:%S')}⢸", Color.BLUE), command)
                print(response or styled_string("- empty response -", italic=True))

                if command == "/stop":
                    logger.debug("Break loop")
                    break

    except Exception as error:
        loader.stop()
        logger.error(error, exc_info=True)
        print(
            styled_string("Connection error", Color.RED),
            styled_string("| Check latest.log for more details", Color.BLACK),
        )

    except KeyboardInterrupt:
        loader.stop()
        logger.critical("Forced shutdown by user")
        print(styled_string("\033[2K\rForced shutdown by user", Color.LIGHT_RED))
