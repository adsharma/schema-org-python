from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.action import Action


@dataclass
class SolveMathAction(Action):
    """
    The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.
    """

    eduQuestionType: Optional[Union[str, List[str]]] = None
