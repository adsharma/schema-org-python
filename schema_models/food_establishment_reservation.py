from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.reservation import Reservation


class FoodEstablishmentReservation(Reservation):
    startTime: Optional[Union[datetime, List[datetime]]] = None
    startTime: Optional[Union[time, List[time]]] = None
    endTime: Optional[Union[datetime, List[datetime]]] = None
    endTime: Optional[Union[time, List[time]]] = None
    partySize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    partySize: Optional[Union[int, List[int]]] = None
