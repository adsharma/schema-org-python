from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.delivery_method import DeliveryMethod
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class SendAction(TransferAction):
    """
    The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:

    * [[ReceiveAction]]: The reciprocal of SendAction.
    * [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).
    """

    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            ContactPoint,
            List[ContactPoint],
            Person,
            List[Person],
            Organization,
            List[Organization],
        ]
    ] = None
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
