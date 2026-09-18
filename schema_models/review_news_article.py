from dataclasses import dataclass

from schema_models.critic_review import CriticReview


@dataclass
class ReviewNewsArticle(CriticReview):
    """
    A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
