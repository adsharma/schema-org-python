from typing import List, Optional, Union

from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.price_specification import PriceSpecification
from schema_models.program_membership import ProgramMembership
from schema_models.reservation_status_type import ReservationStatusType
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.ticket import Ticket


class Reservation(Intangible):
    totalPrice: Optional[Union[Text, List[Text]]] = None
    totalPrice: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    totalPrice: Optional[Union[Number, List[Number]]] = None
    underName: Optional[Union[Person, List[Person]]] = None
    underName: Optional[Union[Organization, List[Organization]]] = None
    programMembershipUsed: Optional[
        Union[ProgramMembership, List[ProgramMembership]]
    ] = None
    bookingTime: Optional[Union[DateTime, List[DateTime]]] = None
    reservationFor: Optional[Union[Thing, List[Thing]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
    reservedTicket: Optional[Union[Ticket, List[Ticket]]] = None
    reservationStatus: Optional[
        Union[ReservationStatusType, List[ReservationStatusType]]
    ] = None
    reservationId: Optional[Union[Text, List[Text]]] = None
    modifiedTime: Optional[Union[DateTime, List[DateTime]]] = None
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    bookingAgent: Optional[Union[Person, List[Person]]] = None
    bookingAgent: Optional[Union[Organization, List[Organization]]] = None
