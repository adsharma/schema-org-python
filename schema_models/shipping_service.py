from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.fulfillment_type_enumeration import FulfillmentTypeEnumeration
from schema_models.member_program_tier import MemberProgramTier
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service_period import ServicePeriod
from schema_models.shipping_conditions import ShippingConditions
from schema_models.structured_value import StructuredValue


@dataclass
class ShippingService(StructuredValue):
    """
    ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer.
    """

    fulfillmentType: Optional[
        Union[FulfillmentTypeEnumeration, List[FulfillmentTypeEnumeration]]
    ] = None
    handlingTime: Optional[
        Union[
            QuantitativeValue,
            List[QuantitativeValue],
            ServicePeriod,
            List[ServicePeriod],
        ]
    ] = None
    shippingConditions: Optional[
        Union[ShippingConditions, List[ShippingConditions]]
    ] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
