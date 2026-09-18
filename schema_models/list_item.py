from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


@dataclass
class ListItem(Intangible):
    """
    An list item, e.g. a step in a checklist or how-to description.
    """

    item: Optional[Union[Thing, List[Thing]]] = None
    nextItem: Optional[Union["ListItem", List["ListItem"]]] = None
    position: Optional[Union[int, List[int], str, List[str]]] = None
    previousItem: Optional[Union["ListItem", List["ListItem"]]] = None
