from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.price_specification import PriceSpecification
from schema_models.seat import Seat
from schema_models.text import Text
from schema_models.url import URL


class Ticket(Intangible):
    dateIssued: Optional[Union[Date, List[Date]]] = None
    dateIssued: Optional[Union[DateTime, List[DateTime]]] = None
    ticketToken: Optional[Union[Text, List[Text]]] = None
    ticketToken: Optional[Union[URL, List[URL]]] = None
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    ticketedSeat: Optional[Union[Seat, List[Seat]]] = None
    ticketNumber: Optional[Union[Text, List[Text]]] = None
    totalPrice: Optional[Union[Text, List[Text]]] = None
    totalPrice: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    totalPrice: Optional[Union[Number, List[Number]]] = None
    underName: Optional[Union[Person, List[Person]]] = None
    underName: Optional[Union[Organization, List[Organization]]] = None
