from typing import List, Optional, Union

from schema_models.intangible import Intangible


class MemberProgramTier(Intangible):
    isTierOf: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    hasTierRequirement: Optional[Union["CreditCard", List["CreditCard"]]] = None
    hasTierRequirement: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    hasTierRequirement: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    hasTierRequirement: Optional[Union[str, List[str]]] = None
    hasTierBenefit: Optional[
        Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]
    ] = None
    membershipPointsEarned: Optional[Union[float, List[float]]] = None
    membershipPointsEarned: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
