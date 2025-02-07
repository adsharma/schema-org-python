from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL


class VisualArtwork(CreativeWork):
    penciler: Optional[Union[Person, List[Person]]] = None
    width: Optional[Union["Distance", List["Distance"]]] = None
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    artform: Optional[Union[Text, List[Text]]] = None
    artform: Optional[Union[URL, List[URL]]] = None
    surface: Optional[Union[URL, List[URL]]] = None
    surface: Optional[Union[Text, List[Text]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
    depth: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    depth: Optional[Union["Distance", List["Distance"]]] = None
    artEdition: Optional[Union[Integer, List[Integer]]] = None
    artEdition: Optional[Union[Text, List[Text]]] = None
    inker: Optional[Union[Person, List[Person]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    artworkSurface: Optional[Union[Text, List[Text]]] = None
    artworkSurface: Optional[Union[URL, List[URL]]] = None
    artMedium: Optional[Union[Text, List[Text]]] = None
    artMedium: Optional[Union[URL, List[URL]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
