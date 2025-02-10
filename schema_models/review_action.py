from typing import List, Optional, Union

from schema_models.assess_action import AssessAction
from schema_models.review import Review


class ReviewAction(AssessAction):
    """
    The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.
    """

    resultReview: Optional[Union[Review, List[Review]]] = None
