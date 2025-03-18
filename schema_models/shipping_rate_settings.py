from typing import List, Optional, Union

from schema_models.defined_region import DefinedRegion
from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class ShippingRateSettings(StructuredValue):
    """
    A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].
    """

    shippingLabel: Optional[Union[str, List[str]]] = None
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = None
    freeShippingThreshold: Optional[
        Union[
            "DeliveryChargeSpecification",
            List["DeliveryChargeSpecification"],
            MonetaryAmount,
            List[MonetaryAmount],
        ]
    ] = None
    doesNotShip: Optional[Union[bool, List[bool]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
