from typing import List, Optional, Union

from schema_models.product import Product


class IndividualProduct(Product):
    serialNumber: Optional[Union[str, List[str]]] = None
