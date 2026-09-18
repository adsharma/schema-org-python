from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.price_component_type_enumeration import PriceComponentTypeEnumeration
from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration
from schema_models.quantitative_value import QuantitativeValue


@dataclass
class UnitPriceSpecification(PriceSpecification):
    """
    The price asked for a given offer by the respective organization or person.
    """

    billingDuration: Optional[
        Union[
            Duration,
            List[Duration],
            float,
            List[float],
            QuantitativeValue,
            List[QuantitativeValue],
        ]
    ] = None
    billingIncrement: Optional[Union[float, List[float]]] = None
    billingStart: Optional[Union[float, List[float]]] = None
    priceComponentType: Optional[
        Union[PriceComponentTypeEnumeration, List[PriceComponentTypeEnumeration]]
    ] = None
    priceType: Optional[
        Union[PriceTypeEnumeration, List[PriceTypeEnumeration], str, List[str]]
    ] = None
    referenceQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    unitCode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    unitText: Optional[Union[str, List[str]]] = None
