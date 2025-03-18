from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


class VisualArtwork(CreativeWork):
    """
    A work of art that is primarily visual in character.
    """

    penciler: Optional[Union[Person, List[Person]]] = None
    width: Optional[
        Union[
            "Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]
        ]
    ] = None
    artform: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    surface: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
    depth: Optional[
        Union[
            "QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]
        ]
    ] = None
    artEdition: Optional[Union[int, List[int], str, List[str]]] = None
    inker: Optional[Union[Person, List[Person]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    artworkSurface: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    artMedium: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    height: Optional[
        Union[
            "Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]
        ]
    ] = None
