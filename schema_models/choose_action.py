from typing import List, Optional, Union

from schema_models.assess_action import AssessAction
from schema_models.text import Text
from schema_models.thing import Thing


class ChooseAction(AssessAction):
    actionOption: Optional[Union[Thing, List[Thing]]] = None
    actionOption: Optional[Union[Text, List[Text]]] = None
    option: Optional[Union[Thing, List[Thing]]] = None
    option: Optional[Union[Text, List[Text]]] = None
