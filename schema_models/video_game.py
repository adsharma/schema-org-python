from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.game import Game
from schema_models.game_server import GameServer
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.thing import Thing


@dataclass
class VideoGame(Game):
    """
    A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.
    """

    actor: Optional[
        Union[PerformingGroup, List[PerformingGroup], Person, List[Person]]
    ] = None
    actors: Optional[Union[Person, List[Person]]] = None
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    gameEdition: Optional[Union[str, List[str]]] = None
    gamePlatform: Optional[
        Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]
    ] = None
    gameServer: Optional[Union[GameServer, List[GameServer]]] = None
    gameTip: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = (
        None
    )
    playMode: Optional[Union["GamePlayMode", List["GamePlayMode"]]] = None
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = None
