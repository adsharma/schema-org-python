from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.product import Product
from schema_models.text import Text


class ProductGroup(Product):
    productGroupID: Optional[Union[Text, List[Text]]] = None
    hasVariant: Optional[Union[Product, List[Product]]] = None
    variesBy: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    variesBy: Optional[Union[Text, List[Text]]] = None
