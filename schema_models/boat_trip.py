from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.trip import Trip


@dataclass
class BoatTrip(Trip):
    """
    A trip on a commercial ferry line.
    """

    arrivalBoatTerminal: Optional[Union["BoatTerminal", List["BoatTerminal"]]] = None
    departureBoatTerminal: Optional[Union["BoatTerminal", List["BoatTerminal"]]] = None
