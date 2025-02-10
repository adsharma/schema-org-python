from typing import List, Optional, Union

from schema_models.comment import Comment
from schema_models.communicate_action import CommunicateAction


class CommentAction(CommunicateAction):
    """
    The act of generating a comment about a subject.
    """

    resultComment: Optional[Union[Comment, List[Comment]]] = None
