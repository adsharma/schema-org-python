from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.member_program import MemberProgram


@dataclass
class MemberProgramTier(Intangible):
    """
    A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".
    """

    hasTierBenefit: Optional[
        Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]
    ] = None
    hasTierRequirement: Optional[
        Union[
            "CreditCard",
            List["CreditCard"],
            "MonetaryAmount",
            List["MonetaryAmount"],
            str,
            List[str],
            "UnitPriceSpecification",
            List["UnitPriceSpecification"],
        ]
    ] = None
    isTierOf: Optional[Union[MemberProgram, List[MemberProgram]]] = None
    membershipPointsEarned: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
