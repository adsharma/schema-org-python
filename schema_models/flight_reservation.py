from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.reservation import Reservation
from schema_models.text import Text


class FlightReservation(Reservation):
    boardingGroup: Optional[Union[Text, List[Text]]] = None
    passengerPriorityStatus: Optional[
        Union[QualitativeValue, List[QualitativeValue]]
    ] = None
    passengerPriorityStatus: Optional[Union[Text, List[Text]]] = None
    passengerSequenceNumber: Optional[Union[Text, List[Text]]] = None
    securityScreening: Optional[Union[Text, List[Text]]] = None
