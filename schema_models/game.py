from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.place import Place
from schema_models.thing import Thing


class Game(CreativeWork):
    """
    The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.
    """

    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    characterAttribute: Optional[Union[Thing, List[Thing]]] = None
    gameItem: Optional[Union[Thing, List[Thing]]] = None
    quest: Optional[Union[Thing, List[Thing]]] = None
    gameLocation: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            "PostalAddress",
            List["PostalAddress"],
            Place,
            List[Place],
        ]
    ] = None
