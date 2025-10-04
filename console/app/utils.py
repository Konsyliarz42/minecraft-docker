import argparse
import logging
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile


def get_logger() -> logging.Logger:
    log_file_path = Path("logs/latest.log")

    if log_file_path.exists():
        with open(log_file_path, "r") as file:
            first_line = file.readline()

        if first_line:
            _, iso_date = first_line.rsplit(" ", 1)
            log_zip_path = Path(f"logs/{datetime.fromisoformat(iso_date.strip()).strftime('%d-%m-%Y-%H-%M-%S')}.zip")
            with ZipFile(log_zip_path, "w") as zip_file:
                zip_file.write(log_file_path)

            log_file_path.write_text("")
    else:
        log_file_path.parent.mkdir(exist_ok=True)

    formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)8s | %(message)s", datefmt="%H:%M:%S")

    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("ConsoleApp")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger


def get_client_configuration() -> dict[str, str | int]:
    parser = argparse.ArgumentParser(prog="Console App")

    parser.add_argument("--host", required=True, help="host of the RCON server")
    parser.add_argument("--port", required=True, help="port of the RCON server", type=int)
    parser.add_argument("--password", required=True, help="password to authenticate with RCON server")
    parser.add_argument("--timeout", required=False, help="timeout (in seconds) for RCON response", type=float)

    args = parser.parse_args()

    return {
        "host": args.host,
        "port": args.port,
        "passwd": args.password,
        "timeout": args.timeout,
    }
