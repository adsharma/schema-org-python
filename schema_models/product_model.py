from typing import List, Optional, Union

from schema_models.product import Product


class ProductModel(Product):
    """
    A datasheet or vendor specification of a product (in the sense of a prototypical description).
    """

    successorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductGroup", List["ProductGroup"]]] = None
    predecessorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
