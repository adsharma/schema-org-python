from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.quantitative_value import QuantitativeValue
from schema_models.thing import Thing
from schema_models.url import URL


class Game(CreativeWork):
    numberOfPlayers: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    quest: Optional[Union[Thing, List[Thing]]] = None
    gameLocation: Optional[Union[URL, List[URL]]] = None
    gameLocation: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    gameLocation: Optional[Union[Place, List[Place]]] = None
