from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class GameServerStatus(StatusEnumeration):
    """
    Status of a game server.
    """
