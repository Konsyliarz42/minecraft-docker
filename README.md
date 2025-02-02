# Minecraft Docker

Docker wrapper for Minecraft servers with few server tools.

## Getting started

1. Download this repository.
2. Create `.env` file form `example.env`.
3. Set the variables inside `.env` file.
4. Build docker image from compose:

   ```bash
   docker compose build
   ```

5. Run docker compose:
   ```bash
   docker compose up -d
   ```

## Configuration

Every single start the container `eula.txt` and `server.properties` are recreated from `.env` file.

### Required variables

| Key             | Type      | Default | Description                                                                                                                                           |
| --------------- | --------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RCON_PASSWORD` | _string_  | -       | Password for RCON protocol.                                                                                                                           |
| `SERVER_JAR`    | _string_  | -       | Any executable server [.jar](https://minecraft.wiki/w/Server.jar) file. Must be in `data` directory.                                                  |
| `EULA`          | _boolean_ | `false` | Microsoft end-user license agreement. You have to agree if you want start the server. For more information read [this](https://aka.ms/MinecraftEULA). |
| `MAX_MEMORY`    | _string_  | `2G`    | Exactly the same as `-Xmx` for [`java`](https://docs.oracle.com/en/java/javase/23/docs/specs/man/java.html) command.                                  |

### Optional variables

| Key            | Type     | Default   | Description                                                                                    |
| -------------- | -------- | --------- | ---------------------------------------------------------------------------------------------- |
| `RCON_TIMEOUT` | _float_  | -         | The connection timeout (in seconds) used in the console. An empty value indicating no timeout. |
| `RCON_HOST`    | _string_ | 127.0.0.1 | Host of the RCON server.                                                                       |

A description of every other server property can be found on the [wiki page](https://minecraft.wiki/w/Server.properties?oldid=2724135).

> There is one exception to the wiki: `ENABLE_RCON` is default `true`

### Extra properties

If your server jar require additional properties add them to `data/extra.properties`.

## Console

You can access to server console by using command:

```bash
docker compose exec minecraft console
```

The commands what are you can using are defined by your server type.

> To close console use `exit` command.

## Server logs

To check logs run simple logs command:

```bash
docker compose logs -f
```
