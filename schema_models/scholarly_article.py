from dataclasses import dataclass

from schema_models.article import Article


@dataclass
class ScholarlyArticle(Article):
    """
    A scholarly article.
    """
