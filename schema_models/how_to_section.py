from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class HowToSection(CreativeWork):
    """
    A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).
    """

    steps: Optional[
        Union[
            CreativeWork,
            List[CreativeWork],
            "ItemList",
            List["ItemList"],
            str,
            List[str],
        ]
    ] = None
