from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class ListItem(Intangible):
    """
    An list item, e.g. a step in a checklist or how-to description.
    """

    position: Optional[Union[str, List[str], int, List[int]]] = None
    previousItem: Optional[Union["ListItem", List["ListItem"]]] = None
    item: Optional[Union[Thing, List[Thing]]] = None
    nextItem: Optional[Union["ListItem", List["ListItem"]]] = None
