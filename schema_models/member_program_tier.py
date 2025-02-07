from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.credit_card import CreditCard
from schema_models.intangible import Intangible
from schema_models.member_program import MemberProgram
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.tier_benefit_enumeration import TierBenefitEnumeration
from schema_models.unit_price_specification import UnitPriceSpecification


class MemberProgramTier(Intangible):
    isTierOf: Optional[Union[MemberProgram, List[MemberProgram]]] = None
    hasTierRequirement: Optional[Union[CreditCard, List[CreditCard]]] = None
    hasTierRequirement: Optional[
        Union[UnitPriceSpecification, List[UnitPriceSpecification]]
    ] = None
    hasTierRequirement: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    hasTierRequirement: Optional[Union[Text, List[Text]]] = None
    hasTierBenefit: Optional[
        Union[TierBenefitEnumeration, List[TierBenefitEnumeration]]
    ] = None
    membershipPointsEarned: Optional[Union[Number, List[Number]]] = None
    membershipPointsEarned: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
