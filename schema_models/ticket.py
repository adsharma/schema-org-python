from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.seat import Seat


class Ticket(Intangible):
    """
    Used to describe a ticket to an event, a flight, a bus ride, etc.
    """

    dateIssued: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    ticketToken: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    ticketedSeat: Optional[Union[Seat, List[Seat]]] = None
    ticketNumber: Optional[Union[str, List[str]]] = None
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
