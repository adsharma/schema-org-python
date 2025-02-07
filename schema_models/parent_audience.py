from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.number import Number
from schema_models.people_audience import PeopleAudience


class ParentAudience(PeopleAudience):
    childMinAge: Optional[Union[Number, List[Number]]] = None
    childMaxAge: Optional[Union[Number, List[Number]]] = None
