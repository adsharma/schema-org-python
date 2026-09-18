from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.distance import Distance
from schema_models.mass import Mass
from schema_models.person import Person


@dataclass
class VisualArtwork(CreativeWork):
    """
    A work of art that is primarily visual in character.
    """

    artEdition: Optional[Union[int, List[int], str, List[str]]] = None
    artMedium: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    artform: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    artworkSurface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
    depth: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    height: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    surface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    weight: Optional[
        Union[Mass, List[Mass], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    width: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
