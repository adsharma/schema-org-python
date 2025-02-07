from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.game import Game
from schema_models.game_play_mode import GamePlayMode
from schema_models.game_server import GameServer
from schema_models.music_group import MusicGroup
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL
from schema_models.video_object import VideoObject


class VideoGame(Game):
    gameTip: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    gameServer: Optional[Union[GameServer, List[GameServer]]] = None
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    gamePlatform: Optional[Union[Thing, List[Thing]]] = None
    gamePlatform: Optional[Union[Text, List[Text]]] = None
    gamePlatform: Optional[Union[URL, List[URL]]] = None
    gameEdition: Optional[Union[Text, List[Text]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    playMode: Optional[Union[GamePlayMode, List[GamePlayMode]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
