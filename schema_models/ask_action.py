from typing import List, Optional, Union

from schema_models.communicate_action import CommunicateAction
from schema_models.question import Question


class AskAction(CommunicateAction):
    """
    The act of posing a question / favor to someone.

    Related actions:

    * [[ReplyAction]]: Appears generally as a response to AskAction.
    """

    question: Optional[Union[Question, List[Question]]] = None
