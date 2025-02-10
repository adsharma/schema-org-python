from typing import List, Optional, Union

from schema_models.review import Review


class ClaimReview(Review):
    """
    A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).
    """

    claimReviewed: Optional[Union[str, List[str]]] = None
