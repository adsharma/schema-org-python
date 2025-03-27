from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class Collection(CreativeWork):
    """
    A sub property of object. The collection target of the action.
    """

    collectionSize: Optional[Union[int, List[int]]] = None
