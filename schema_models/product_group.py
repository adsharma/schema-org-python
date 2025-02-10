from typing import List, Optional, Union

from schema_models.product import Product


class ProductGroup(Product):
    """
    A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.

    While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]].
    """

    productGroupID: Optional[Union[str, List[str]]] = None
    hasVariant: Optional[Union[Product, List[Product]]] = None
    variesBy: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    variesBy: Optional[Union[str, List[str]]] = None
