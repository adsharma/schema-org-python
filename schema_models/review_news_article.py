from dataclasses import dataclass

from schema_models.news_article import NewsArticle


@dataclass
class ReviewNewsArticle(NewsArticle):
    """
    A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work.
    """
