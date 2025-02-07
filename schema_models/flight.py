from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.airport import Airport
from schema_models.boarding_policy_type import BoardingPolicyType
from schema_models.date_time import DateTime
from schema_models.distance import Distance
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text
from schema_models.trip import Trip
from schema_models.vehicle import Vehicle


class Flight(Trip):
    webCheckinTime: Optional[Union[DateTime, List[DateTime]]] = None
    mealService: Optional[Union[Text, List[Text]]] = None
    arrivalAirport: Optional[Union[Airport, List[Airport]]] = None
    flightNumber: Optional[Union[Text, List[Text]]] = None
    flightDistance: Optional[Union[Text, List[Text]]] = None
    flightDistance: Optional[Union[Distance, List[Distance]]] = None
    departureAirport: Optional[Union[Airport, List[Airport]]] = None
    carrier: Optional[Union[Organization, List[Organization]]] = None
    aircraft: Optional[Union[Vehicle, List[Vehicle]]] = None
    aircraft: Optional[Union[Text, List[Text]]] = None
    departureTerminal: Optional[Union[Text, List[Text]]] = None
    arrivalTerminal: Optional[Union[Text, List[Text]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    departureGate: Optional[Union[Text, List[Text]]] = None
    arrivalGate: Optional[Union[Text, List[Text]]] = None
    estimatedFlightDuration: Optional[Union[Text, List[Text]]] = None
    estimatedFlightDuration: Optional[Union[Duration, List[Duration]]] = None
    boardingPolicy: Optional[Union[BoardingPolicyType, List[BoardingPolicyType]]] = None
