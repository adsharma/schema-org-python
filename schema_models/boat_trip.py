from typing import List, Optional, Union

from schema_models.trip import Trip


class BoatTrip(Trip):
    departureBoatTerminal: Optional[Union["BoatTerminal", List["BoatTerminal"]]] = None
    arrivalBoatTerminal: Optional[Union["BoatTerminal", List["BoatTerminal"]]] = None
