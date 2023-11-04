from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

PROPERTIES_PATH = Path("server.properties")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    server_host: str
    server_port: int
    rcon_server: bool
    rcon_port: int
    rcon_password: str


if __name__ == "__main__":
    settings = Settings()  # type: ignore
    
    PROPERTIES_PATH.touch()
    properties = PROPERTIES_PATH.read_text("utf-8").split("\n")
    properties_to_set = [
        f"enable-rcon={str(settings.rcon_server).lower()}",
        f"rcon.password={settings.rcon_password}",
        f"rcon.port={settings.rcon_port}",
        f"server-ip={settings.server_host}",
        f"server-port={settings.server_port}",
    ]
    property_names = [prop.split("=")[0] for prop in properties_to_set]
    new_properties = []

    for prop in properties:
        if "#" in prop or any(True for name in property_names if name in prop):
            continue

        new_properties.append(prop)

    new_properties = new_properties + properties_to_set
    PROPERTIES_PATH.write_text("\n".join(new_properties))
