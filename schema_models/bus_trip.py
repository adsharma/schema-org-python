from typing import List, Optional, Union

from schema_models.text import Text
from schema_models.trip import Trip


class BusTrip(Trip):
    departureBusStop: Optional[Union["BusStation", List["BusStation"]]] = None
    departureBusStop: Optional[Union["BusStop", List["BusStop"]]] = None
    arrivalBusStop: Optional[Union["BusStop", List["BusStop"]]] = None
    arrivalBusStop: Optional[Union["BusStation", List["BusStation"]]] = None
    busNumber: Optional[Union[Text, List[Text]]] = None
    busName: Optional[Union[Text, List[Text]]] = None
