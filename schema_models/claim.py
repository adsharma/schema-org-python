from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Claim(CreativeWork):
    claimInterpreter: Optional[Union[Person, List[Person]]] = None
    claimInterpreter: Optional[Union[Organization, List[Organization]]] = None
    appearance: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    firstAppearance: Optional[Union[CreativeWork, List[CreativeWork]]] = None
