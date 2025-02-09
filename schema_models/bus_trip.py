from typing import List, Optional, Union

from schema_models.trip import Trip


class BusTrip(Trip):
    departureBusStop: Optional[Union["BusStation", List["BusStation"]]] = None
    departureBusStop: Optional[Union["BusStop", List["BusStop"]]] = None
    arrivalBusStop: Optional[Union["BusStop", List["BusStop"]]] = None
    arrivalBusStop: Optional[Union["BusStation", List["BusStation"]]] = None
    busNumber: Optional[Union[str, List[str]]] = None
    busName: Optional[Union[str, List[str]]] = None
