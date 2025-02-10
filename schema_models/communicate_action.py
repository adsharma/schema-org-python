from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.interact_action import InteractAction
from schema_models.language import Language
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.thing import Thing


class CommunicateAction(InteractAction):
    """
    The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.
    """

    about: Optional[Union[Thing, List[Thing]]] = None
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    recipient: Optional[Union[Audience, List[Audience]]] = None
    recipient: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    recipient: Optional[Union[Person, List[Person]]] = None
    recipient: Optional[Union[Organization, List[Organization]]] = None
    language: Optional[Union[Language, List[Language]]] = None
