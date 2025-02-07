from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.member_program import MemberProgram
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class ProgramMembership(Intangible):
    member: Optional[Union[Person, List[Person]]] = None
    member: Optional[Union[Organization, List[Organization]]] = None
    program: Optional[Union[MemberProgram, List[MemberProgram]]] = None
    programName: Optional[Union[Text, List[Text]]] = None
    membershipPointsEarned: Optional[Union[Number, List[Number]]] = None
    membershipPointsEarned: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    members: Optional[Union[Organization, List[Organization]]] = None
    members: Optional[Union[Person, List[Person]]] = None
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = None
    membershipNumber: Optional[Union[Text, List[Text]]] = None
