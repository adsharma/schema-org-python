from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.communicate_action import CommunicateAction


class ReplyAction(CommunicateAction):
    resultComment: Optional[Union[Comment, List[Comment]]] = None
