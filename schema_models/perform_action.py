from typing import List, Optional, Union

from schema_models.play_action import PlayAction


class PerformAction(PlayAction):
    entertainmentBusiness: Optional[
        Union["EntertainmentBusiness", List["EntertainmentBusiness"]]
    ] = None
