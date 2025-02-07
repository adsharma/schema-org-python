from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.number import Number
from schema_models.price_component_type_enumeration import PriceComponentTypeEnumeration
from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.url import URL


class UnitPriceSpecification(PriceSpecification):
    unitCode: Optional[Union[Text, List[Text]]] = None
    unitCode: Optional[Union[URL, List[URL]]] = None
    unitText: Optional[Union[Text, List[Text]]] = None
    billingDuration: Optional[Union[Number, List[Number]]] = None
    billingDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    billingDuration: Optional[Union[Duration, List[Duration]]] = None
    billingStart: Optional[Union[Number, List[Number]]] = None
    referenceQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    priceType: Optional[Union[PriceTypeEnumeration, List[PriceTypeEnumeration]]] = None
    priceType: Optional[Union[Text, List[Text]]] = None
    priceComponentType: Optional[
        Union[PriceComponentTypeEnumeration, List[PriceComponentTypeEnumeration]]
    ] = None
    billingIncrement: Optional[Union[Number, List[Number]]] = None
