from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.play_action import PlayAction


@dataclass
class PerformAction(PlayAction):
    """
    The act of participating in performance arts.
    """

    entertainmentBusiness: Optional[
        Union["EntertainmentBusiness", List["EntertainmentBusiness"]]
    ] = None
