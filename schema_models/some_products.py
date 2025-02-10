from typing import List, Optional, Union

from schema_models.product import Product


class SomeProducts(Product):
    """
    A placeholder for multiple similar products of the same kind.
    """

    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
