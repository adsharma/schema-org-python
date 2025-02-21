from typing import List, Optional, Union

from schema_models.allocate_action import AllocateAction
from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.organization import Organization
from schema_models.person import Person


class AuthorizeAction(AllocateAction):
    """
    The act of granting permission to an object.
    """

    recipient: Optional[Union[Audience, List[Audience]]] = None
    recipient: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    recipient: Optional[Union[Person, List[Person]]] = None
    recipient: Optional[Union[Organization, List[Organization]]] = None
