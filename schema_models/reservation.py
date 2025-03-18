from datetime import datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


class Reservation(Intangible):
    """
    Describes a reservation for travel, dining or an event. Some reservations require tickets.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]].
    """

    totalPrice: Optional[
        Union[
            str,
            List[str],
            "PriceSpecification",
            List["PriceSpecification"],
            float,
            List[float],
        ]
    ] = None
    underName: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    programMembershipUsed: Optional[
        Union["ProgramMembership", List["ProgramMembership"]]
    ] = None
    bookingTime: Optional[Union[datetime, List[datetime]]] = None
    reservationFor: Optional[Union[Thing, List[Thing]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    reservedTicket: Optional[Union["Ticket", List["Ticket"]]] = None
    reservationStatus: Optional[
        Union["ReservationStatusType", List["ReservationStatusType"]]
    ] = None
    reservationId: Optional[Union[str, List[str]]] = None
    modifiedTime: Optional[Union[datetime, List[datetime]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    provider: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    bookingAgent: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
