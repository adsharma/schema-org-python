from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.defined_region import DefinedRegion
from schema_models.distance import Distance
from schema_models.member_program_tier import MemberProgramTier
from schema_models.monetary_amount import MonetaryAmount
from schema_models.quantitative_value import QuantitativeValue
from schema_models.shipping_delivery_time import ShippingDeliveryTime
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.url import URL


class OfferShippingDetails(StructuredValue):
    shippingSettingsLink: Optional[Union[URL, List[URL]]] = None
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingLabel: Optional[Union[Text, List[Text]]] = None
    height: Optional[Union[Distance, List[Distance]]] = None
    height: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    transitTimeLabel: Optional[Union[Text, List[Text]]] = None
    width: Optional[Union[Distance, List[Distance]]] = None
    width: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    deliveryTime: Optional[Union[ShippingDeliveryTime, List[ShippingDeliveryTime]]] = (
        None
    )
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    depth: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    depth: Optional[Union[Distance, List[Distance]]] = None
    doesNotShip: Optional[Union[Boolean, List[Boolean]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
    shippingRate: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    weight: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
