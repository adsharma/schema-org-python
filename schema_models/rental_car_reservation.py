from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.place import Place
from schema_models.reservation import Reservation


class RentalCarReservation(Reservation):
    pickupTime: Optional[Union[DateTime, List[DateTime]]] = None
    dropoffTime: Optional[Union[DateTime, List[DateTime]]] = None
    dropoffLocation: Optional[Union[Place, List[Place]]] = None
    pickupLocation: Optional[Union[Place, List[Place]]] = None
