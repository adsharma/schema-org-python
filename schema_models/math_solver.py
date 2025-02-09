from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.solve_math_action import SolveMathAction


class MathSolver(CreativeWork):
    mathExpression: Optional[Union[SolveMathAction, List[SolveMathAction]]] = None
    mathExpression: Optional[Union[str, List[str]]] = None
