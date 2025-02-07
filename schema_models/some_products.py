from typing import List, Optional, Union

from schema_models.product import Product
from schema_models.quantitative_value import QuantitativeValue


class SomeProducts(Product):
    inventoryLevel: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
