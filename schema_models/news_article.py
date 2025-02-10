from typing import List, Optional, Union

from schema_models.article import Article


class NewsArticle(Article):
    """
    A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

    A more detailed overview of [schema.org News markup](/docs/news.html) is also available.

    """

    dateline: Optional[Union[str, List[str]]] = None
    printColumn: Optional[Union[str, List[str]]] = None
    printPage: Optional[Union[str, List[str]]] = None
    printEdition: Optional[Union[str, List[str]]] = None
    printSection: Optional[Union[str, List[str]]] = None
