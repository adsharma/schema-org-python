from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.seat import Seat


@dataclass
class Ticket(Intangible):
    """
    Used to describe a ticket to an event, a flight, a bus ride, etc.
    """

    dateIssued: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    ticketNumber: Optional[Union[str, List[str]]] = None
    ticketToken: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    ticketedSeat: Optional[Union[Seat, List[Seat]]] = None
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
