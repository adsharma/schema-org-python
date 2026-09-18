from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration


@dataclass
class HowToDirection(CreativeWork):
    """
    A direction indicating a single action to do in the instructions for how to achieve a result.
    """

    afterMedia: Optional[
        Union["MediaObject", List["MediaObject"], HttpUrl, List[HttpUrl]]
    ] = None
    beforeMedia: Optional[
        Union["MediaObject", List["MediaObject"], HttpUrl, List[HttpUrl]]
    ] = None
    duringMedia: Optional[
        Union["MediaObject", List["MediaObject"], HttpUrl, List[HttpUrl]]
    ] = None
    performTime: Optional[Union[Duration, List[Duration]]] = None
    prepTime: Optional[Union[Duration, List[Duration]]] = None
    supply: Optional[Union["HowToSupply", List["HowToSupply"], str, List[str]]] = None
    tool: Optional[Union["HowToTool", List["HowToTool"], str, List[str]]] = None
    totalTime: Optional[Union[Duration, List[Duration]]] = None
