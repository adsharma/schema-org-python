from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.civic_structure import CivicStructure
from schema_models.person import Person


class EducationalOrganization(CivicStructure):
    alumni: Optional[Union[Person, List[Person]]] = None
