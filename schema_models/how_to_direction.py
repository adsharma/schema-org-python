from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.list_item import ListItem
from schema_models.media_object import MediaObject


class HowToDirection(ListItem):
    """
    A direction indicating a single action to do in the instructions for how to achieve a result.
    """

    supply: Optional[Union[str, List[str], "HowToSupply", List["HowToSupply"]]] = None
    tool: Optional[Union["HowToTool", List["HowToTool"], str, List[str]]] = None
    prepTime: Optional[Union[Duration, List[Duration]]] = None
    totalTime: Optional[Union[Duration, List[Duration]]] = None
    performTime: Optional[Union[Duration, List[Duration]]] = None
    beforeMedia: Optional[
        Union[HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]
    ] = None
    duringMedia: Optional[
        Union[HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]
    ] = None
    afterMedia: Optional[
        Union[HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]
    ] = None
