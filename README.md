# Minecraft Docker

Docker wrapper for **ANY** Minecraft server.

## Requirements

- [Docker compose](https://docs.docker.com/compose/) - `2.30.0` or later.
- Server executable `.jar` file.

## Installation

1. Download or pull this repository.
2. Paste your `.jar` file server inside `server/data`.
3. Create `.env` file from `template.env`.
4. Set variables in the `.env` file.
5. Run docker compose and wait for start server then stop the container.
6. Configure your server in created `server/data/server.properties`.
   > Remember that variables from `.env` override values from `server.properties` when the server starts up.
7. Run docker compose in detached mode:
   ```bash
   docker compose up -d
   ```

## Updating

1. Download or pull the newest version of this repository.
2. Rebuild image:
   ```bash
   docker compose build
   ```
3. Down and up the container:
   ```bash
   docker compose down && docker compose up
   ```

## Sending commands

You can send a command using the `send` command from the Docker image:

```bash
docker compose exec server send <command>
```

or outside the repository:

```bash
docker exec minecraft-server send <command>
```

## Extra - Console App

If you want to sending multiple commands I recommand to use my [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface).

### Requirements

- [Python](https://www.python.org/) - Version is defined [here](console/.python-version).
- [Python dependencies](console/requirements.txt)
- Enabled RCON port in `docker-compose.yaml`

### Usage

Call help command to check how run the app:

```bash
# From `console` directory with activated venv
python -m app --help
```
