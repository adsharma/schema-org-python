from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.solve_math_action import SolveMathAction
from schema_models.text import Text


class MathSolver(CreativeWork):
    mathExpression: Optional[Union[SolveMathAction, List[SolveMathAction]]] = None
    mathExpression: Optional[Union[Text, List[Text]]] = None
