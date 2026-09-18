from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization


@dataclass
class MemberProgram(Intangible):
    """
    A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs may have multiple tiers, for example silver and gold members, each with different benefits.
    """

    hasTiers: Optional[Union["MemberProgramTier", List["MemberProgramTier"]]] = None
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = None
