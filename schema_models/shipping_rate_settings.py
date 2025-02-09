from typing import List, Optional, Union

from schema_models.defined_region import DefinedRegion
from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class ShippingRateSettings(StructuredValue):
    shippingLabel: Optional[Union[str, List[str]]] = None
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = None
    freeShippingThreshold: Optional[
        Union["DeliveryChargeSpecification", List["DeliveryChargeSpecification"]]
    ] = None
    freeShippingThreshold: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    doesNotShip: Optional[Union[bool, List[bool]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
