from typing import List, Optional, Union

from schema_models.product import Product
from schema_models.text import Text


class IndividualProduct(Product):
    serialNumber: Optional[Union[Text, List[Text]]] = None
