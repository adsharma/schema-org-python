from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.gender_type import GenderType
from schema_models.person import Person
from schema_models.sports_organization import SportsOrganization
from schema_models.text import Text


class SportsTeam(SportsOrganization):
    coach: Optional[Union[Person, List[Person]]] = None
    athlete: Optional[Union[Person, List[Person]]] = None
    gender: Optional[Union[GenderType, List[GenderType]]] = None
    gender: Optional[Union[Text, List[Text]]] = None
