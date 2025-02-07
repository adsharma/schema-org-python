from typing import List, Optional, Union

from schema_models.product import Product
from schema_models.type_and_quantity_node import TypeAndQuantityNode


class ProductCollection(Product):
    includesObject: Optional[Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]] = (
        None
    )
