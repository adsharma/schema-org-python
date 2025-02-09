from typing import List, Optional, Union

from schema_models.intangible import Intangible


class Seat(Intangible):
    seatRow: Optional[Union[str, List[str]]] = None
    seatingType: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    seatingType: Optional[Union[str, List[str]]] = None
    seatSection: Optional[Union[str, List[str]]] = None
    seatNumber: Optional[Union[str, List[str]]] = None
