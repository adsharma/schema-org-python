from datetime import datetime
from typing import List, Optional, Union

from schema_models.place import Place
from schema_models.reservation import Reservation


class TaxiReservation(Reservation):
    partySize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    partySize: Optional[Union[int, List[int]]] = None
    pickupTime: Optional[Union[datetime, List[datetime]]] = None
    pickupLocation: Optional[Union[Place, List[Place]]] = None
