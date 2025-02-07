from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.bus_station import BusStation
from schema_models.bus_stop import BusStop
from schema_models.text import Text
from schema_models.trip import Trip


class BusTrip(Trip):
    departureBusStop: Optional[Union[BusStation, List[BusStation]]] = None
    departureBusStop: Optional[Union[BusStop, List[BusStop]]] = None
    arrivalBusStop: Optional[Union[BusStop, List[BusStop]]] = None
    arrivalBusStop: Optional[Union[BusStation, List[BusStation]]] = None
    busNumber: Optional[Union[Text, List[Text]]] = None
    busName: Optional[Union[Text, List[Text]]] = None
