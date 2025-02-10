from typing import List, Optional, Union

from schema_models.product import Product


class IndividualProduct(Product):
    """
    A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """

    serialNumber: Optional[Union[str, List[str]]] = None
