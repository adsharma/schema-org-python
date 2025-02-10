from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.reservation import Reservation


class FlightReservation(Reservation):
    """
    A reservation for air travel.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """

    boardingGroup: Optional[Union[str, List[str]]] = None
    passengerPriorityStatus: Optional[
        Union[QualitativeValue, List[QualitativeValue]]
    ] = None
    passengerPriorityStatus: Optional[Union[str, List[str]]] = None
    passengerSequenceNumber: Optional[Union[str, List[str]]] = None
    securityScreening: Optional[Union[str, List[str]]] = None
