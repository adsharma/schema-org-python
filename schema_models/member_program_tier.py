from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.text import Text


class MemberProgramTier(Intangible):
    isTierOf: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    hasTierRequirement: Optional[Union["CreditCard", List["CreditCard"]]] = None
    hasTierRequirement: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    hasTierRequirement: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    hasTierRequirement: Optional[Union[Text, List[Text]]] = None
    hasTierBenefit: Optional[
        Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]
    ] = None
    membershipPointsEarned: Optional[Union[Number, List[Number]]] = None
    membershipPointsEarned: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
