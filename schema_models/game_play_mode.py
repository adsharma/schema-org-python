from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class GamePlayMode(Enumeration):
    """
    Indicates whether this game is multi-player, co-op or single-player.
    """
