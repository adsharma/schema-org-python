from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.creative_work_season import CreativeWorkSeason
from schema_models.creative_work_series import CreativeWorkSeries
from schema_models.episode import Episode
from schema_models.hyper_toc_entry import HyperTocEntry
from schema_models.integer import Integer
from schema_models.music_group import MusicGroup
from schema_models.number import Number
from schema_models.performing_group import PerformingGroup
from schema_models.person import Person
from schema_models.text import Text


class Clip(CreativeWork):
    musicBy: Optional[Union[Person, List[Person]]] = None
    musicBy: Optional[Union[MusicGroup, List[MusicGroup]]] = None
    partOfSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = None
    clipNumber: Optional[Union[Text, List[Text]]] = None
    clipNumber: Optional[Union[Integer, List[Integer]]] = None
    actor: Optional[Union[Person, List[Person]]] = None
    actor: Optional[Union[PerformingGroup, List[PerformingGroup]]] = None
    director: Optional[Union[Person, List[Person]]] = None
    actors: Optional[Union[Person, List[Person]]] = None
    endOffset: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = None
    endOffset: Optional[Union[Number, List[Number]]] = None
    startOffset: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = None
    startOffset: Optional[Union[Number, List[Number]]] = None
    directors: Optional[Union[Person, List[Person]]] = None
    partOfEpisode: Optional[Union[Episode, List[Episode]]] = None
    partOfSeries: Optional[Union[CreativeWorkSeries, List[CreativeWorkSeries]]] = None
