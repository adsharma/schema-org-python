from typing import List, Optional, Union

from schema_models.gender_type import GenderType
from schema_models.person import Person
from schema_models.sports_organization import SportsOrganization


class SportsTeam(SportsOrganization):
    """
    A sub property of participant. The sports team that participated on this action.
    """

    coach: Optional[Union[Person, List[Person]]] = None
    athlete: Optional[Union[Person, List[Person]]] = None
    gender: Optional[Union[GenderType, List[GenderType]]] = None
    gender: Optional[Union[str, List[str]]] = None
