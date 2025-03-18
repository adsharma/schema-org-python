from typing import List, Optional, Union

from schema_models.trip import Trip


class BusTrip(Trip):
    """
    A trip on a commercial bus line.
    """

    departureBusStop: Optional[
        Union["BusStation", List["BusStation"], "BusStop", List["BusStop"]]
    ] = None
    arrivalBusStop: Optional[
        Union["BusStop", List["BusStop"], "BusStation", List["BusStation"]]
    ] = None
    busNumber: Optional[Union[str, List[str]]] = None
    busName: Optional[Union[str, List[str]]] = None
