from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.inform_action import InformAction
from schema_models.rsvp_response_type import RsvpResponseType


class RsvpAction(InformAction):
    """
    The act of notifying an event organizer as to whether you expect to attend the event.
    """

    rsvpResponse: Optional[Union[RsvpResponseType, List[RsvpResponseType]]] = None
    additionalNumberOfGuests: Optional[Union[float, List[float]]] = None
    comment: Optional[Union[Comment, List[Comment]]] = None
