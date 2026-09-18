from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_region import DefinedRegion
from schema_models.distance import Distance
from schema_models.mass import Mass
from schema_models.member_program_tier import MemberProgramTier
from schema_models.monetary_amount import MonetaryAmount
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.structured_value import StructuredValue


@dataclass
class OfferShippingDetails(StructuredValue):
    """
    OfferShippingDetails represents information about shipping destinations.

    Multiple of these entities can be used to represent different shipping rates for different destinations:

    One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

    Multiple of these entities can be used to represent different shipping costs and delivery times.

    Two entities that are identical but differ in rate and time:

    E.g. Cheaper and slower: $5 in 5-7 days
    or Fast and expensive: $15 in 1-2 days.
    """

    deliveryTime: Optional[
        Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]
    ] = None
    depth: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    doesNotShip: Optional[Union[bool, List[bool]]] = None
    hasShippingService: Optional[Union["ShippingService", List["ShippingService"]]] = (
        None
    )
    height: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingLabel: Optional[Union[str, List[str]]] = None
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[
        Union[
            MonetaryAmount,
            List[MonetaryAmount],
            "ShippingRateSettings",
            List["ShippingRateSettings"],
        ]
    ] = None
    shippingSettingsLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    transitTimeLabel: Optional[Union[str, List[str]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    weight: Optional[
        Union[Mass, List[Mass], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    width: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
