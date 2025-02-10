from typing import List, Optional, Union

from schema_models.product import Product


class ProductCollection(Product):
    """
    A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]].
    """

    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
