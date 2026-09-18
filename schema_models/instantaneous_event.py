from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue
from schema_models.thing import Thing


@dataclass
class InstantaneousEvent(StructuredValue):
    """
    An event with no duration, like for instance a computer log entry.
    """

    data: Optional[Union[Thing, List[Thing]]] = None
    source: Optional[Union[Thing, List[Thing]]] = None
    timestamp: Optional[Union[datetime, List[datetime]]] = None
