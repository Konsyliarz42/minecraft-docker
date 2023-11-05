# Minecraft Docker

## Getting started

1. Download this repository
2. Create a `.env` file from the `example.env` file.
3. Set the variables inside the `.env` file.
   - **SERVER_HOST** : _string_ - Server IP | _default: 0.0.0.0_.
   - **SERVER_PORT** : _string_ - Server port | _Default: 25565_
   - **SERVER_JAR** : _string_ - Path to the `.jar` executable file.
   - **SERVER_MAX_MEMORY** : _string_ - Maximum RAM for the server | _Default: 2G_
   - **RCON_SERVER** : _boolean_ - Run RCON server, this variable is required for [remote console](#remote-console) | _Default: true_.
   - **RCON_PORT** : _integer_ - RCON server port | _Default: 25575_
   - **RCON_PASSWORD** : _string_ - RCON server password.
4. Create a `data` directory for the server files
5. Prepare the server inside `data` directory.
   > Properties such as: `enable-rcon`, `rcon.password`, `rcon.port`, `server-ip`, `server-port`
   > are set to values from the `.env` file each time the container is started.
6. Build the docker image:
   ```bash
   docker build -t minecraft-docker .
   ```
7. Run docker compose:
   ```bash
   docker compose up -d
   ```

## Remote Console

> Only if you have set `RCON_SERVER` to `true`\*\*!

To open the console in docker, use this command:

```bash
docker compose exec minecraft ../console.sh
```

or you can use `remote_console.py` from this repo:

```bash
pip install rcon # This is the dependency for this module
python remote_console.py
```
