from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.reservation import Reservation


@dataclass
class LodgingReservation(Reservation):
    """
    A reservation for lodging at a hotel, motel, inn, etc.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """

    checkinTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    checkoutTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    lodgingUnitDescription: Optional[Union[str, List[str]]] = None
    lodgingUnitType: Optional[
        Union[QualitativeValue, List[QualitativeValue], str, List[str]]
    ] = None
    numAdults: Optional[
        Union[int, List[int], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numChildren: Optional[
        Union[int, List[int], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
