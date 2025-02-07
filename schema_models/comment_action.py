from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.comment import Comment
from schema_models.communicate_action import CommunicateAction


class CommentAction(CommunicateAction):
    resultComment: Optional[Union[Comment, List[Comment]]] = None
