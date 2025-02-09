from typing import List, Optional, Union

from schema_models.action import Action


class SeekToAction(Action):
    startOffset: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
    startOffset: Optional[Union[float, List[float]]] = None
