from typing import List, Optional, Union

from schema_models.date_time import DateTime
from schema_models.integer import Integer
from schema_models.place import Place
from schema_models.reservation import Reservation


class TaxiReservation(Reservation):
    partySize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    partySize: Optional[Union[Integer, List[Integer]]] = None
    pickupTime: Optional[Union[DateTime, List[DateTime]]] = None
    pickupLocation: Optional[Union[Place, List[Place]]] = None
