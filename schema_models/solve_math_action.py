from typing import List, Optional, Union

from schema_models.action import Action


class SolveMathAction(Action):
    eduQuestionType: Optional[Union[str, List[str]]] = None
