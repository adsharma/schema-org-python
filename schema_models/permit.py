from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization


class Permit(Intangible):
    issuedThrough: Optional[Union["Service", List["Service"]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    validUntil: Optional[Union[date, List[date]]] = None
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    permitAudience: Optional[Union["Audience", List["Audience"]]] = None
    validFor: Optional[Union["Duration", List["Duration"]]] = None
