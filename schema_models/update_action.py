from typing import List, Optional, Union

from schema_models.action import Action
from schema_models.thing import Thing


class UpdateAction(Action):
    collection: Optional[Union[Thing, List[Thing]]] = None
    targetCollection: Optional[Union[Thing, List[Thing]]] = None
