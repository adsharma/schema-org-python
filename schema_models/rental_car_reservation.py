from datetime import datetime
from typing import List, Optional, Union

from schema_models.place import Place
from schema_models.reservation import Reservation


class RentalCarReservation(Reservation):
    pickupTime: Optional[Union[datetime, List[datetime]]] = None
    dropoffTime: Optional[Union[datetime, List[datetime]]] = None
    dropoffLocation: Optional[Union[Place, List[Place]]] = None
    pickupLocation: Optional[Union[Place, List[Place]]] = None
