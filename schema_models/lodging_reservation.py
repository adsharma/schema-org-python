from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.reservation import Reservation


class LodgingReservation(Reservation):
    """
    A reservation for lodging at a hotel, motel, inn, etc.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """

    numChildren: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], int, List[int]]
    ] = None
    lodgingUnitDescription: Optional[Union[str, List[str]]] = None
    lodgingUnitType: Optional[
        Union[QualitativeValue, List[QualitativeValue], str, List[str]]
    ] = None
    checkoutTime: Optional[Union[time, List[time], datetime, List[datetime]]] = None
    numAdults: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], int, List[int]]
    ] = None
    checkinTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
