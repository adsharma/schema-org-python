from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.integer import Integer


class GameServer(Intangible):
    serverStatus: Optional[Union["GameServerStatus", List["GameServerStatus"]]] = None
    game: Optional[Union["VideoGame", List["VideoGame"]]] = None
    playersOnline: Optional[Union[Integer, List[Integer]]] = None
