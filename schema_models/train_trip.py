from typing import List, Optional, Union

from schema_models.text import Text
from schema_models.train_station import TrainStation
from schema_models.trip import Trip


class TrainTrip(Trip):
    arrivalStation: Optional[Union[TrainStation, List[TrainStation]]] = None
    departureStation: Optional[Union[TrainStation, List[TrainStation]]] = None
    departurePlatform: Optional[Union[Text, List[Text]]] = None
    arrivalPlatform: Optional[Union[Text, List[Text]]] = None
    trainNumber: Optional[Union[Text, List[Text]]] = None
    trainName: Optional[Union[Text, List[Text]]] = None
