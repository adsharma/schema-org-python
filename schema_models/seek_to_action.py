from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.number import Number


class SeekToAction(Action):
    startOffset: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
    startOffset: Optional[Union[Number, List[Number]]] = None
