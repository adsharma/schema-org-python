from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.reservation import Reservation


class FoodEstablishmentReservation(Reservation):
    """
    A reservation to dine at a food-related business.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """

    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    partySize: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], int, List[int]]
    ] = None
