from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.member_program_tier import MemberProgramTier
from schema_models.structured_value import StructuredValue


class PriceSpecification(StructuredValue):
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    valueAddedTaxIncluded: Optional[Union[bool, List[bool]]] = None
    maxPrice: Optional[Union[float, List[float]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
    membershipPointsEarned: Optional[Union[float, List[float]]] = None
    membershipPointsEarned: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    price: Optional[Union[str, List[str]]] = None
    price: Optional[Union[float, List[float]]] = None
    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    minPrice: Optional[Union[float, List[float]]] = None
