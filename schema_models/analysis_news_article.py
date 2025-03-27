from dataclasses import dataclass

from schema_models.news_article import NewsArticle


@dataclass
class AnalysisNewsArticle(NewsArticle):
    """
    An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions.
    """
