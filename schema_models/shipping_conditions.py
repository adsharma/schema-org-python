from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.defined_region import DefinedRegion
from schema_models.distance import Distance
from schema_models.mass import Mass
from schema_models.monetary_amount import MonetaryAmount
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service_period import ServicePeriod
from schema_models.structured_value import StructuredValue


@dataclass
class ShippingConditions(StructuredValue):
    """
    The conditions (constraints, price) applicable to the [[ShippingService]].
    """

    depth: Optional[
        Union[Distance, List[Distance], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    doesNotShip: Optional[Union[bool, List[bool]]] = None
    height: Optional[
        Union[Distance, List[Distance], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numItems: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    orderValue: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    seasonalOverride: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[
        Union[
            MonetaryAmount,
            List[MonetaryAmount],
            "ShippingRateSettings",
            List["ShippingRateSettings"],
        ]
    ] = None
    transitTime: Optional[
        Union[
            QuantitativeValue,
            List[QuantitativeValue],
            ServicePeriod,
            List[ServicePeriod],
        ]
    ] = None
    weight: Optional[
        Union[Mass, List[Mass], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    width: Optional[
        Union[Distance, List[Distance], QuantitativeValue, List[QuantitativeValue]]
    ] = None
