from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.thing import Thing


class Game(CreativeWork):
    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    quest: Optional[Union[Thing, List[Thing]]] = None
    gameLocation: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    gameLocation: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    gameLocation: Optional[Union[Place, List[Place]]] = None
