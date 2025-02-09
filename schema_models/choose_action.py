from typing import List, Optional, Union

from schema_models.assess_action import AssessAction
from schema_models.thing import Thing


class ChooseAction(AssessAction):
    actionOption: Optional[Union[Thing, List[Thing]]] = None
    actionOption: Optional[Union[str, List[str]]] = None
    option: Optional[Union[Thing, List[Thing]]] = None
    option: Optional[Union[str, List[str]]] = None
