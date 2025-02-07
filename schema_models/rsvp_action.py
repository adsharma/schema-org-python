from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.comment import Comment
from schema_models.inform_action import InformAction
from schema_models.number import Number
from schema_models.rsvp_response_type import RsvpResponseType


class RsvpAction(InformAction):
    rsvpResponse: Optional[Union[RsvpResponseType, List[RsvpResponseType]]] = None
    additionalNumberOfGuests: Optional[Union[Number, List[Number]]] = None
    comment: Optional[Union[Comment, List[Comment]]] = None
