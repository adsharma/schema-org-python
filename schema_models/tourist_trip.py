from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.trip import Trip


class TouristTrip(Trip):
    touristType: Optional[Union[str, List[str]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
