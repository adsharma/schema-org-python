from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.react_action import ReactAction


class EndorseAction(ReactAction):
    endorsee: Optional[Union[Person, List[Person]]] = None
    endorsee: Optional[Union[Organization, List[Organization]]] = None
