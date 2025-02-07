from typing import List, Optional, Union

from schema_models.product import Product
from schema_models.product_group import ProductGroup


class ProductModel(Product):
    successorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union[ProductGroup, List[ProductGroup]]] = None
    predecessorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
