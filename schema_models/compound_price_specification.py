from typing import List, Optional, Union

from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration
from schema_models.text import Text
from schema_models.unit_price_specification import UnitPriceSpecification


class CompoundPriceSpecification(PriceSpecification):
    priceComponent: Optional[
        Union[UnitPriceSpecification, List[UnitPriceSpecification]]
    ] = None
    priceType: Optional[Union[PriceTypeEnumeration, List[PriceTypeEnumeration]]] = None
    priceType: Optional[Union[Text, List[Text]]] = None
