from typing import List, Optional, Union

from schema_models.intangible import Intangible


class GameServer(Intangible):
    """
    The server on which  it is possible to play the game.
    """

    serverStatus: Optional[Union["GameServerStatus", List["GameServerStatus"]]] = None
    game: Optional[Union["VideoGame", List["VideoGame"]]] = None
    playersOnline: Optional[Union[int, List[int]]] = None
