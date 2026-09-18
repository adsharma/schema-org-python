from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.organization import Organization


@dataclass
class Permit(Intangible):
    """
    A permit issued by an organization, e.g. a parking pass.
    """

    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    issuedThrough: Optional[Union["Service", List["Service"]]] = None
    permitAudience: Optional[Union[Audience, List[Audience]]] = None
    validFor: Optional[Union[Duration, List[Duration]]] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
    validUntil: Optional[Union[date, List[date]]] = None
