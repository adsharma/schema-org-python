from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.member_program_tier import MemberProgramTier
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class PriceSpecification(StructuredValue):
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    valueAddedTaxIncluded: Optional[Union[Boolean, List[Boolean]]] = None
    maxPrice: Optional[Union[Number, List[Number]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
    membershipPointsEarned: Optional[Union[Number, List[Number]]] = None
    membershipPointsEarned: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    price: Optional[Union[Text, List[Text]]] = None
    price: Optional[Union[Number, List[Number]]] = None
    eligibleQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    minPrice: Optional[Union[Number, List[Number]]] = None
