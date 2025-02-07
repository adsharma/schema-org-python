from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.text import Text
from schema_models.trip import Trip


class TouristTrip(Trip):
    touristType: Optional[Union[Text, List[Text]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
