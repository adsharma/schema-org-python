from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_region import DefinedRegion
from schema_models.distance import Distance
from schema_models.member_program_tier import MemberProgramTier
from schema_models.monetary_amount import MonetaryAmount
from schema_models.structured_value import StructuredValue


class OfferShippingDetails(StructuredValue):
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
