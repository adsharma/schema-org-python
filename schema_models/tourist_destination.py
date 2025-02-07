from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.place import Place
from schema_models.text import Text
from schema_models.tourist_attraction import TouristAttraction


class TouristDestination(Place):
    touristType: Optional[Union[Text, List[Text]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    includesAttraction: Optional[Union[TouristAttraction, List[TouristAttraction]]] = (
        None
    )
