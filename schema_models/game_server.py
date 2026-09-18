from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class GameServer(Intangible):
    """
    The server on which  it is possible to play the game.
    """

    game: Optional[Union["VideoGame", List["VideoGame"]]] = None
    playersOnline: Optional[Union[int, List[int]]] = None
    serverStatus: Optional[Union["GameServerStatus", List["GameServerStatus"]]] = None
