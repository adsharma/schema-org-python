from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.communicate_action import CommunicateAction
from schema_models.question import Question


class AskAction(CommunicateAction):
    question: Optional[Union[Question, List[Question]]] = None
