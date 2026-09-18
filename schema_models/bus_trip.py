from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.trip import Trip


@dataclass
class BusTrip(Trip):
    """
    A trip on a commercial bus line.
    """

    arrivalBusStop: Optional[
        Union["BusStation", List["BusStation"], "BusStop", List["BusStop"]]
    ] = None
    busName: Optional[Union[str, List[str]]] = None
    busNumber: Optional[Union[str, List[str]]] = None
    departureBusStop: Optional[
        Union["BusStation", List["BusStation"], "BusStop", List["BusStop"]]
    ] = None
