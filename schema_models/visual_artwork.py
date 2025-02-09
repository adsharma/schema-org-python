from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


class VisualArtwork(CreativeWork):
    penciler: Optional[Union[Person, List[Person]]] = None
    width: Optional[Union["Distance", List["Distance"]]] = None
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    artform: Optional[Union[str, List[str]]] = None
    artform: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    surface: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    surface: Optional[Union[str, List[str]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
    depth: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    depth: Optional[Union["Distance", List["Distance"]]] = None
    artEdition: Optional[Union[int, List[int]]] = None
    artEdition: Optional[Union[str, List[str]]] = None
    inker: Optional[Union[Person, List[Person]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    artworkSurface: Optional[Union[str, List[str]]] = None
    artworkSurface: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    artMedium: Optional[Union[str, List[str]]] = None
    artMedium: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
