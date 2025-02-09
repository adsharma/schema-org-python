from datetime import datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


class Reservation(Intangible):
    totalPrice: Optional[Union[str, List[str]]] = None
    totalPrice: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = None
    totalPrice: Optional[Union[float, List[float]]] = None
    underName: Optional[Union[Person, List[Person]]] = None
    underName: Optional[Union[Organization, List[Organization]]] = None
    programMembershipUsed: Optional[
        Union["ProgramMembership", List["ProgramMembership"]]
    ] = None
    bookingTime: Optional[Union[datetime, List[datetime]]] = None
    reservationFor: Optional[Union[Thing, List[Thing]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
    reservedTicket: Optional[Union["Ticket", List["Ticket"]]] = None
    reservationStatus: Optional[
        Union["ReservationStatusType", List["ReservationStatusType"]]
    ] = None
    reservationId: Optional[Union[str, List[str]]] = None
    modifiedTime: Optional[Union[datetime, List[datetime]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    bookingAgent: Optional[Union[Person, List[Person]]] = None
    bookingAgent: Optional[Union[Organization, List[Organization]]] = None
