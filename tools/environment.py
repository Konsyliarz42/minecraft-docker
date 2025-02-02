from enum import Enum
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Difficulty(str, Enum):
    EASY = "easy"
    HARD = "hard"
    NORMAL = "normal"
    PEACEFUL = "peaceful"


class DifficultyLegacy(int, Enum):
    EASY = 1
    HARD = 3
    NORMAL = 2
    PEACEFUL = 0


class GameMode(str, Enum):
    ADVENTURE = "adventure"
    CREATIVE = "creative"
    SPECTATOR = "spectator"
    SURVIVAL = "survival"


class GameModeLegacy(int, Enum):
    ADVENTURE = 2
    CREATIVE = 1
    SPECTATOR = 3
    SURVIVAL = 0


class LevelType(str, Enum):
    AMPLIFIED = "amplified"
    FLAT = "flat"
    LARGE_BIOMES = "large_biomes"
    MINECRAFT_AMPLIFIED = "minecraft:amplified"
    MINECRAFT_FLAT = "minecraft:flat"
    MINECRAFT_LARGE_BIOMES = "minecraft:large_biomes"
    MINECRAFT_NORMAL = "minecraft:normal"
    MINECRAFT_SINGLE_BIOME_SURFACE = "minecraft:single_biome_surface"
    NORMAL = "normal"
    SINGLE_BIOME_SURFACE = "single_biome_surface"


class CompressionAlgorithm(str, Enum):
    DEFLATE = "deflate"
    LZ4 = "lz4"
    NONE = "none"


class Properties(BaseSettings):
    """
    Server properties for 1.21.1
    Based on: https://minecraft.wiki/w/Server.properties?oldid=2724135
    """

    accepts_transfers: bool = Field(serialization_alias="accepts-transfers", default=False)
    allow_flight: bool = Field(serialization_alias="allow-flight", default=False)
    allow_nether: bool = Field(serialization_alias="allow-nether", default=True)
    broadcast_console_to_ops: bool = Field(
        serialization_alias="broadcast-console-to-ops", default=True
    )
    broadcast_rcon_to_ops: bool = Field(serialization_alias="broadcast-rcon-to-ops", default=True)
    bug_report_link: str = Field(serialization_alias="bug-report-link", default="")
    difficulty: Difficulty | DifficultyLegacy = Field(default=Difficulty.EASY)
    enable_command_block: bool = Field(serialization_alias="enable-command-block", default=False)
    enable_jmx_monitoring: bool = Field(serialization_alias="enable-jmx-monitoring", default=False)
    enable_query: bool = Field(serialization_alias="enable-query", default=False)
    enable_rcon: bool = Field(serialization_alias="enable-rcon", default=True)
    enable_status: bool = Field(serialization_alias="enable-status", default=True)
    enforce_secure_profile: bool = Field(serialization_alias="enforce-secure-profile", default=True)
    enforce_whitelist: bool = Field(serialization_alias="enforce-whitelist", default=False)
    entity_broadcast_range_percentage: int = Field(
        serialization_alias="entity-broadcast-range-percentage", default=100, ge=10, le=1000
    )
    force_gamemode: bool = Field(serialization_alias="force-gamemode", default=False)
    function_permission_level: int = Field(
        serialization_alias="function-permission-level", default=2, ge=1, le=4
    )
    gamemode: GameMode | GameModeLegacy = Field(default=GameMode.SURVIVAL)
    generate_structures: bool = Field(serialization_alias="generate-structures", default=True)
    generator_settings: str = Field(serialization_alias="generator-settings", default="{}")
    hardcore: bool = Field(default=False)
    hide_online_players: bool = Field(serialization_alias="hide-online-players", default=False)
    initial_disabled_packs: str = Field(serialization_alias="initial-disabled-packs", default="")
    initial_enabled_packs: str = Field(
        serialization_alias="initial-enabled-packs", default="vanilla"
    )
    level_name: str = Field(serialization_alias="level-name", default="world")
    level_seed: str = Field(serialization_alias="level-seed", default="")
    level_type: LevelType = Field(
        serialization_alias="level-type", default=LevelType.MINECRAFT_NORMAL
    )
    log_ips: bool = Field(serialization_alias="log-ips", default=True)
    max_chained_neighbor_updates: int = Field(
        serialization_alias="max-chained-neighbor-updates", default=1000000
    )
    max_players: int = Field(serialization_alias="max-players", default=20, ge=0, le=(2**31) - 1)
    max_tick_time: int = Field(
        serialization_alias="max-tick-time", default=60000, ge=-1, le=(2**63) - 1
    )
    max_world_size: int = Field(
        serialization_alias="max-world-size", default=29999984, ge=1, le=29999984
    )
    motd: str = Field(default="A Minecraft Server", max_length=59)
    network_compression_threshold: int = Field(
        serialization_alias="network-compression-threshold", default=256, ge=-1
    )
    online_mode: bool = Field(serialization_alias="online-mode", default=True)
    op_permission_level: int = Field(
        serialization_alias="op-permission-level", default=4, ge=0, le=4
    )
    pause_when_empty_seconds: int = Field(
        serialization_alias="pause-when-empty-seconds", default=60
    )
    player_idle_timeout: int = Field(serialization_alias="player-idle-timeout", default=0)
    prevent_proxy_connections: bool = Field(
        serialization_alias="prevent-proxy-connections", default=False
    )
    pvp: bool = Field(default=True)
    query_port: int = Field(serialization_alias="query.port", default=25565, ge=1, le=(2**16) - 2)
    rate_limit: int = Field(serialization_alias="rate-limit", default=0)
    rcon_password: str = Field(serialization_alias="rcon.password")
    rcon_port: int = Field(serialization_alias="rcon.port", default=25575, ge=1, le=(2**16) - 2)
    region_file_compression: CompressionAlgorithm = Field(
        serialization_alias="region-file-compression", default=CompressionAlgorithm.DEFLATE
    )
    require_resource_pack: bool = Field(serialization_alias="require-resource-pack", default=False)
    resource_pack: str = Field(serialization_alias="resource-pack", default="")
    resource_pack_prompt: str = Field(serialization_alias="resource-pack-prompt", default="")
    resource_pack_sha1: str = Field(serialization_alias="resource-pack-sha1", default="")
    server_ip: str = Field(serialization_alias="server-ip", default="")
    server_port: int = Field(serialization_alias="server-port", default=25565, ge=1, le=(2**16) - 2)
    simulation_distance: int = Field(
        serialization_alias="simulation-distance", default=10, ge=3, le=32
    )
    spawn_monsters: bool = Field(serialization_alias="spawn-monsters", default=True)
    spawn_protection: int = Field(serialization_alias="spawn-protection", default=16, ge=0)
    sync_chunk_writes: bool = Field(serialization_alias="sync-chunk-writes", default=True)
    text_filtering_config: str = Field(
        serialization_alias="text-filtering-config", default=""
    )  # More information needed
    use_native_transport: bool = Field(serialization_alias="use-native-transport", default=True)
    view_distance: int = Field(serialization_alias="view-distance", default=10, ge=3, le=32)
    white_list: bool = Field(serialization_alias="white-list", default=False)


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    eula: bool = Field(default=False)
    max_memory: str = Field(pattern=r"^\d*[gGmMkK]$")
    rcon_host: Optional[str] = Field(default="127.0.0.1")
    rcon_timeout: Optional[float] = Field(default=None, gt=0)
    server_jar: str = Field()

    server_properties: Properties = Field(default_factory=Properties)
