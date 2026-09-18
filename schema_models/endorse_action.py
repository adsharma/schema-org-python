from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.react_action import ReactAction


@dataclass
class EndorseAction(ReactAction):
    """
    An agent approves/certifies/likes/supports/sanctions an object.
    """

    endorsee: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
