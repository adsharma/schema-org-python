from datetime import datetime
from typing import List, Optional, Union

from schema_models.boarding_policy_type import BoardingPolicyType
from schema_models.distance import Distance
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.trip import Trip
from schema_models.vehicle import Vehicle


class Flight(Trip):
    """
    An airline flight.
    """

    webCheckinTime: Optional[Union[datetime, List[datetime]]] = None
    mealService: Optional[Union[str, List[str]]] = None
    arrivalAirport: Optional[Union["Airport", List["Airport"]]] = None
    flightNumber: Optional[Union[str, List[str]]] = None
    flightDistance: Optional[Union[str, List[str], Distance, List[Distance]]] = None
    departureAirport: Optional[Union["Airport", List["Airport"]]] = None
    carrier: Optional[Union[Organization, List[Organization]]] = None
    aircraft: Optional[Union[Vehicle, List[Vehicle], str, List[str]]] = None
    departureTerminal: Optional[Union[str, List[str]]] = None
    arrivalTerminal: Optional[Union[str, List[str]]] = None
    seller: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    departureGate: Optional[Union[str, List[str]]] = None
    arrivalGate: Optional[Union[str, List[str]]] = None
    estimatedFlightDuration: Optional[
        Union[str, List[str], Duration, List[Duration]]
    ] = None
    boardingPolicy: Optional[Union[BoardingPolicyType, List[BoardingPolicyType]]] = None
