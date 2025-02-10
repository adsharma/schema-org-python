from typing import List, Optional, Union

from schema_models.achieve_action import AchieveAction
from schema_models.person import Person


class WinAction(AchieveAction):
    """
    The act of achieving victory in a competitive activity.
    """

    loser: Optional[Union[Person, List[Person]]] = None
