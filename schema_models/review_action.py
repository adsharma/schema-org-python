from typing import List, Optional, Union

from schema_models.assess_action import AssessAction
from schema_models.review import Review


class ReviewAction(AssessAction):
    resultReview: Optional[Union[Review, List[Review]]] = None
