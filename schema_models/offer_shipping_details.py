from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_region import DefinedRegion
from schema_models.distance import Distance
from schema_models.member_program_tier import MemberProgramTier
from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


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

    shippingSettingsLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingLabel: Optional[Union[str, List[str]]] = None
    height: Optional[Union[Distance, List[Distance]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    transitTimeLabel: Optional[Union[str, List[str]]] = None
    width: Optional[Union[Distance, List[Distance]]] = None
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    deliveryTime: Optional[
        Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]
    ] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    depth: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    depth: Optional[Union[Distance, List[Distance]]] = None
    doesNotShip: Optional[Union[bool, List[bool]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
