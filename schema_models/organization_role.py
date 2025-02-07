from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.number import Number
from schema_models.role import Role


class OrganizationRole(Role):
    numberedPosition: Optional[Union[Number, List[Number]]] = None
