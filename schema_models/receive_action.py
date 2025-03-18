from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.delivery_method import DeliveryMethod
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class ReceiveAction(TransferAction):
    """
    The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.

    Related actions:

    * [[SendAction]]: The reciprocal of ReceiveAction.
    * [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).
    """

    sender: Optional[
        Union[
            Organization,
            List[Organization],
            Audience,
            List[Audience],
            Person,
            List[Person],
        ]
    ] = None
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = None
