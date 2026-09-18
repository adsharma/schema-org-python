from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.boarding_policy_type import BoardingPolicyType
from schema_models.distance import Distance
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trip import Trip
from schema_models.vehicle import Vehicle


@dataclass
class Flight(Trip):
    """
    An airline flight.
    """

    aircraft: Optional[Union[str, List[str], Vehicle, List[Vehicle]]] = None
    arrivalAirport: Optional[Union["Airport", List["Airport"]]] = None
    arrivalGate: Optional[Union[str, List[str]]] = None
    arrivalTerminal: Optional[Union[str, List[str]]] = None
    boardingPolicy: Optional[Union[BoardingPolicyType, List[BoardingPolicyType]]] = None
    carrier: Optional[Union[Organization, List[Organization]]] = None
    departureAirport: Optional[Union["Airport", List["Airport"]]] = None
    departureGate: Optional[Union[str, List[str]]] = None
    departureTerminal: Optional[Union[str, List[str]]] = None
    estimatedFlightDuration: Optional[
        Union[Duration, List[Duration], str, List[str]]
    ] = None
    flightDistance: Optional[Union[Distance, List[Distance], str, List[str]]] = None
    flightNumber: Optional[Union[str, List[str]]] = None
    mealService: Optional[Union[str, List[str]]] = None
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    webCheckinTime: Optional[Union[datetime, List[datetime]]] = None
