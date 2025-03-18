from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.solve_math_action import SolveMathAction


class MathSolver(CreativeWork):
    """
    A math solver which is capable of solving a subset of mathematical problems.
    """

    mathExpression: Optional[
        Union[SolveMathAction, List[SolveMathAction], str, List[str]]
    ] = None
