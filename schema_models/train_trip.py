from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.trip import Trip


@dataclass
class TrainTrip(Trip):
    """
    A trip on a commercial train line.
    """

    arrivalPlatform: Optional[Union[str, List[str]]] = None
    arrivalStation: Optional[Union["TrainStation", List["TrainStation"]]] = None
    departurePlatform: Optional[Union[str, List[str]]] = None
    departureStation: Optional[Union["TrainStation", List["TrainStation"]]] = None
    trainName: Optional[Union[str, List[str]]] = None
    trainNumber: Optional[Union[str, List[str]]] = None
