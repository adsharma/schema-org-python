from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.thing import Thing


@dataclass
class Game(CreativeWork):
    """
    Video game which is played on this server.
    """

    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    gameLocation: Optional[
        Union[
            Place,
            List[Place],
            "PostalAddress",
            List["PostalAddress"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    quest: Optional[Union[Thing, List[Thing]]] = None
