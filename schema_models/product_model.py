from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.product import Product
from schema_models.product_group import ProductGroup


@dataclass
class ProductModel(Product):
    """
    A datasheet or vendor specification of a product (in the sense of a prototypical description).
    """

    isVariantOf: Optional[
        Union[ProductGroup, List[ProductGroup], "ProductModel", List["ProductModel"]]
    ] = None
    predecessorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    successorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
