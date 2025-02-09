from typing import List, Optional, Union

from schema_models.review import Review


class ClaimReview(Review):
    claimReviewed: Optional[Union[str, List[str]]] = None
