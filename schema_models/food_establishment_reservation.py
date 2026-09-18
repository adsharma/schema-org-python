from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.reservation import Reservation


@dataclass
class FoodEstablishmentReservation(Reservation):
    """
    A reservation to dine at a food-related business.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """

    endTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    partySize: Optional[
        Union[int, List[int], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    startTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
