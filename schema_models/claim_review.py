from typing import List, Optional, Union

from schema_models.review import Review
from schema_models.text import Text


class ClaimReview(Review):
    claimReviewed: Optional[Union[Text, List[Text]]] = None
