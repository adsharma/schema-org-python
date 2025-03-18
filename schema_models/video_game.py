from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.game import Game
from schema_models.game_play_mode import GamePlayMode
from schema_models.game_server import GameServer
from schema_models.music_group import MusicGroup
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.thing import Thing
from schema_models.video_object import VideoObject


class VideoGame(Game):
    """
    A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.
    """

    gameTip: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    musicBy: Optional[Union[Person, List[Person], MusicGroup, List[MusicGroup]]] = None
    gameServer: Optional[Union[GameServer, List[GameServer]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    actor: Optional[
        Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]
    ] = None
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    gamePlatform: Optional[
        Union[Thing, List[Thing], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    gameEdition: Optional[Union[str, List[str]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    playMode: Optional[Union[GamePlayMode, List[GamePlayMode]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
