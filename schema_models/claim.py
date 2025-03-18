from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Claim(CreativeWork):
    """
    A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized with the [[text]] property. Variations on well known claims can have their common identity indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]] description includes enough contextual information to minimize the risk of ambiguity or inclarity. In practice, many claims are better understood in the context in which they appear or the interpretations provided by claim reviews.

      Beyond [[ClaimReview]], the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]] or [[Question]] might be [[about]] some [[Claim]].

      At this time, Schema.org does not define any types of relationship between claims. This is a natural area for future exploration.

    """

    claimInterpreter: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    appearance: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    firstAppearance: Optional[Union[CreativeWork, List[CreativeWork]]] = None
