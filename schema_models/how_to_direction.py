from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.list_item import ListItem
from schema_models.media_object import MediaObject
from schema_models.text import Text
from schema_models.url import URL


class HowToDirection(ListItem):
    supply: Optional[Union[Text, List[Text]]] = None
    supply: Optional[Union["HowToSupply", List["HowToSupply"]]] = None
    tool: Optional[Union["HowToTool", List["HowToTool"]]] = None
    tool: Optional[Union[Text, List[Text]]] = None
    prepTime: Optional[Union[Duration, List[Duration]]] = None
    totalTime: Optional[Union[Duration, List[Duration]]] = None
    performTime: Optional[Union[Duration, List[Duration]]] = None
    beforeMedia: Optional[Union[URL, List[URL]]] = None
    beforeMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    duringMedia: Optional[Union[URL, List[URL]]] = None
    duringMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    afterMedia: Optional[Union[URL, List[URL]]] = None
    afterMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
