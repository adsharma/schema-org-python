from typing import List, Optional, Union

from schema_models.assess_action import AssessAction
from schema_models.thing import Thing


class ChooseAction(AssessAction):
    """
    The act of expressing a preference from a set of options or a large or unbounded set of choices/options.
    """

    actionOption: Optional[Union[Thing, List[Thing], str, List[str]]] = None
    option: Optional[Union[Thing, List[Thing], str, List[str]]] = None
