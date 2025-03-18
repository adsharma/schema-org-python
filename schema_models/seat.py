from typing import List, Optional, Union

from schema_models.intangible import Intangible


class Seat(Intangible):
    """
    Used to describe a seat, such as a reserved seat in an event reservation.
    """

    seatRow: Optional[Union[str, List[str]]] = None
    seatingType: Optional[
        Union["QualitativeValue", List["QualitativeValue"], str, List[str]]
    ] = None
    seatSection: Optional[Union[str, List[str]]] = None
    seatNumber: Optional[Union[str, List[str]]] = None
