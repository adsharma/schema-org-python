from typing import List, Optional, Union

from schema_models.communicate_action import CommunicateAction
from schema_models.question import Question


class AskAction(CommunicateAction):
    question: Optional[Union[Question, List[Question]]] = None
