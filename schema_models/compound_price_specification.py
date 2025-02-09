from typing import List, Optional, Union

from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration


class CompoundPriceSpecification(PriceSpecification):
    priceComponent: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    priceType: Optional[Union[PriceTypeEnumeration, List[PriceTypeEnumeration]]] = None
    priceType: Optional[Union[str, List[str]]] = None
