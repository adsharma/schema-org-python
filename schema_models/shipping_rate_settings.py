from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.defined_region import DefinedRegion
from schema_models.delivery_charge_specification import DeliveryChargeSpecification
from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class ShippingRateSettings(StructuredValue):
    shippingLabel: Optional[Union[Text, List[Text]]] = None
    isUnlabelledFallback: Optional[Union[Boolean, List[Boolean]]] = None
    freeShippingThreshold: Optional[
        Union[DeliveryChargeSpecification, List[DeliveryChargeSpecification]]
    ] = None
    freeShippingThreshold: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    doesNotShip: Optional[Union[Boolean, List[Boolean]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
