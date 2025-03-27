from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.achieve_action import AchieveAction
from schema_models.person import Person


@dataclass
class LoseAction(AchieveAction):
    """
    The act of being defeated in a competitive activity.
    """

    winner: Optional[Union[Person, List[Person]]] = None
