from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.communicate_action import CommunicateAction


class ReplyAction(CommunicateAction):
    """
    The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].

    Related actions:

    * [[AskAction]]: Appears generally as an origin of a ReplyAction.
    """

    resultComment: Optional[Union[Comment, List[Comment]]] = None
