from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


class ProgramMembership(Intangible):
    member: Optional[Union[Person, List[Person]]] = None
    member: Optional[Union[Organization, List[Organization]]] = None
    program: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    programName: Optional[Union[str, List[str]]] = None
    membershipPointsEarned: Optional[Union[float, List[float]]] = None
    membershipPointsEarned: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    members: Optional[Union[Organization, List[Organization]]] = None
    members: Optional[Union[Person, List[Person]]] = None
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = None
    membershipNumber: Optional[Union[str, List[str]]] = None
