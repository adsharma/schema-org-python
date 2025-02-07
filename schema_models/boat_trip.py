from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boat_terminal import BoatTerminal
from schema_models.trip import Trip


class BoatTrip(Trip):
    departureBoatTerminal: Optional[Union[BoatTerminal, List[BoatTerminal]]] = None
    arrivalBoatTerminal: Optional[Union[BoatTerminal, List[BoatTerminal]]] = None
