from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.collection import Collection


@dataclass
class ProductCollection(Collection):
    """
    A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """

    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
