from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.organization import Organization
from schema_models.service import Service
from schema_models.text import Text


class GovernmentService(Service):
    serviceOperator: Optional[Union[Organization, List[Organization]]] = None
    jurisdiction: Optional[Union[Text, List[Text]]] = None
    jurisdiction: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
