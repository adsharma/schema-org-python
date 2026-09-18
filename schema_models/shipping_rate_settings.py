from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.defined_region import DefinedRegion
from schema_models.monetary_amount import MonetaryAmount
from schema_models.price_specification import PriceSpecification
from schema_models.structured_value import StructuredValue


@dataclass
class ShippingRateSettings(StructuredValue):
    """
    A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].
    """

    doesNotShip: Optional[Union[bool, List[bool]]] = None
    freeShippingThreshold: Optional[
        Union[
            "DeliveryChargeSpecification",
            List["DeliveryChargeSpecification"],
            MonetaryAmount,
            List[MonetaryAmount],
        ]
    ] = None
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = None
    minimumOrderValue: Optional[
        Union[
            MonetaryAmount,
            List[MonetaryAmount],
            float,
            List[float],
            PriceSpecification,
            List[PriceSpecification],
        ]
    ] = None
    orderPercentage: Optional[Union[float, List[float]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingLabel: Optional[Union[str, List[str]]] = None
    shippingRate: Optional[
        Union[
            MonetaryAmount,
            List[MonetaryAmount],
            "ShippingRateSettings",
            List["ShippingRateSettings"],
        ]
    ] = None
    weightPercentage: Optional[Union[float, List[float]]] = None
