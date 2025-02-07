from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.delivery_method import DeliveryMethod
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class ReceiveAction(TransferAction):
    sender: Optional[Union[Organization, List[Organization]]] = None
    sender: Optional[Union[Audience, List[Audience]]] = None
    sender: Optional[Union[Person, List[Person]]] = None
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
