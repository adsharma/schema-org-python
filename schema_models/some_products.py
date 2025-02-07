from typing import List, Optional, Union

from schema_models.product import Product


class SomeProducts(Product):
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
