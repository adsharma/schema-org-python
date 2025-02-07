from typing import List, Optional, Union

from schema_models.game_server_status import GameServerStatus
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.video_game import VideoGame


class GameServer(Intangible):
    serverStatus: Optional[Union[GameServerStatus, List[GameServerStatus]]] = None
    game: Optional[Union[VideoGame, List[VideoGame]]] = None
    playersOnline: Optional[Union[Integer, List[Integer]]] = None
