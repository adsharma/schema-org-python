from typing import List, Optional, Union

from schema_models.product import Product


class ProductCollection(Product):
    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
