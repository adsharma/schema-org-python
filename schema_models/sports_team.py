from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.gender_type import GenderType
from schema_models.person import Person
from schema_models.sports_organization import SportsOrganization


@dataclass
class SportsTeam(SportsOrganization):
    """
    A sub property of participant. The sports team that participated on this action.
    """

    athlete: Optional[Union[Person, List[Person]]] = None
    coach: Optional[Union[Person, List[Person]]] = None
    gender: Optional[Union[GenderType, List[GenderType], str, List[str]]] = None
