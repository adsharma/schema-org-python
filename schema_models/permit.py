from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.audience import Audience
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.service import Service


class Permit(Intangible):
    issuedThrough: Optional[Union[Service, List[Service]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    validUntil: Optional[Union[Date, List[Date]]] = None
    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    permitAudience: Optional[Union[Audience, List[Audience]]] = None
    validFor: Optional[Union[Duration, List[Duration]]] = None
