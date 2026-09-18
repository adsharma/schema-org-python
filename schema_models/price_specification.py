from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.member_program_tier import MemberProgramTier
from schema_models.structured_value import StructuredValue


@dataclass
class PriceSpecification(StructuredValue):
    """
    One or more detailed price specifications, indicating the unit price and delivery or payment charges.
    """

    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    maxPrice: Optional[Union[float, List[float]]] = None
    membershipPointsEarned: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    minPrice: Optional[Union[float, List[float]]] = None
    price: Optional[Union[float, List[float], str, List[str]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    valueAddedTaxIncluded: Optional[Union[bool, List[bool]]] = None
