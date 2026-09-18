from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.member_program import MemberProgram
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class ProgramMembership(Intangible):
    """
    Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.
    """

    hostingOrganization: Optional[Union[Organization, List[Organization]]] = None
    member: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    members: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    membershipNumber: Optional[Union[str, List[str]]] = None
    membershipPointsEarned: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    program: Optional[Union[MemberProgram, List[MemberProgram]]] = None
    programName: Optional[Union[str, List[str]]] = None
