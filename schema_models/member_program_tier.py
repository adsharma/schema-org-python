from typing import List, Optional, Union

from schema_models.intangible import Intangible


class MemberProgramTier(Intangible):
    """
    A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".
    """

    isTierOf: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    hasTierRequirement: Optional[
        Union[
            "CreditCard",
            List["CreditCard"],
            "UnitPriceSpecification",
            List["UnitPriceSpecification"],
            "MonetaryAmount",
            List["MonetaryAmount"],
            str,
            List[str],
        ]
    ] = None
    hasTierBenefit: Optional[
        Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]
    ] = None
    membershipPointsEarned: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
