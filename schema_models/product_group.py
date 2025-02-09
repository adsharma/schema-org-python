from typing import List, Optional, Union

from schema_models.product import Product


class ProductGroup(Product):
    productGroupID: Optional[Union[str, List[str]]] = None
    hasVariant: Optional[Union[Product, List[Product]]] = None
    variesBy: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    variesBy: Optional[Union[str, List[str]]] = None
