from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.reservation import Reservation


class ReservationPackage(Reservation):
    subReservation: Optional[Union[Reservation, List[Reservation]]] = None
