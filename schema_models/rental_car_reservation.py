from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.place import Place
from schema_models.reservation import Reservation


@dataclass
class RentalCarReservation(Reservation):
    """
    A reservation for a rental car.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """

    dropoffLocation: Optional[Union[Place, List[Place]]] = None
    dropoffTime: Optional[Union[datetime, List[datetime]]] = None
    pickupLocation: Optional[Union[Place, List[Place]]] = None
    pickupTime: Optional[Union[datetime, List[datetime]]] = None
