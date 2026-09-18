from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.program_membership import ProgramMembership
from schema_models.thing import Thing


@dataclass
class Reservation(Intangible):
    """
    Describes a reservation for travel, dining or an event. Some reservations require tickets.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]].
    """

    bookingAgent: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    bookingTime: Optional[Union[datetime, List[datetime]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    modifiedTime: Optional[Union[datetime, List[datetime]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    programMembershipUsed: Optional[
        Union[ProgramMembership, List[ProgramMembership]]
    ] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    reservationFor: Optional[Union[Thing, List[Thing]]] = None
    reservationId: Optional[Union[str, List[str]]] = None
    reservationStatus: Optional[
        Union["ReservationStatusType", List["ReservationStatusType"]]
    ] = None
    reservedTicket: Optional[Union["Ticket", List["Ticket"]]] = None
    totalPrice: Optional[
        Union[
            float,
            List[float],
            "PriceSpecification",
            List["PriceSpecification"],
            str,
            List[str],
        ]
    ] = None
    underName: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
