from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.number import Number
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text
from schema_models.transfer_action import TransferAction


class DonateAction(TransferAction):
    price: Optional[Union[Text, List[Text]]] = None
    price: Optional[Union[Number, List[Number]]] = None
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    priceSpecification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    recipient: Optional[Union[Audience, List[Audience]]] = None
    recipient: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    recipient: Optional[Union[Person, List[Person]]] = None
    recipient: Optional[Union[Organization, List[Organization]]] = None
