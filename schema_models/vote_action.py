from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.choose_action import ChooseAction
from schema_models.person import Person


@dataclass
class VoteAction(ChooseAction):
    """
    The act of expressing a preference from a fixed/finite/structured set of choices/options.
    """

    candidate: Optional[Union[Person, List[Person]]] = None
