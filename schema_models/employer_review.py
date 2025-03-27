from dataclasses import dataclass

from schema_models.review import Review


@dataclass
class EmployerReview(Review):
    """
    An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.
    """
