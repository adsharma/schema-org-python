from typing import List, Optional, Union

from schema_models.trip import Trip


class TrainTrip(Trip):
    """
    A trip on a commercial train line.
    """

    arrivalStation: Optional[Union["TrainStation", List["TrainStation"]]] = None
    departureStation: Optional[Union["TrainStation", List["TrainStation"]]] = None
    departurePlatform: Optional[Union[str, List[str]]] = None
    arrivalPlatform: Optional[Union[str, List[str]]] = None
    trainNumber: Optional[Union[str, List[str]]] = None
    trainName: Optional[Union[str, List[str]]] = None
