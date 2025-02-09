from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.price_component_type_enumeration import PriceComponentTypeEnumeration
from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration
from schema_models.quantitative_value import QuantitativeValue


class UnitPriceSpecification(PriceSpecification):
    unitCode: Optional[Union[str, List[str]]] = None
    unitCode: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    unitText: Optional[Union[str, List[str]]] = None
    billingDuration: Optional[Union[float, List[float]]] = None
    billingDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    billingDuration: Optional[Union[Duration, List[Duration]]] = None
    billingStart: Optional[Union[float, List[float]]] = None
    referenceQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    priceType: Optional[Union[PriceTypeEnumeration, List[PriceTypeEnumeration]]] = None
    priceType: Optional[Union[str, List[str]]] = None
    priceComponentType: Optional[
        Union[PriceComponentTypeEnumeration, List[PriceComponentTypeEnumeration]]
    ] = None
    billingIncrement: Optional[Union[float, List[float]]] = None
