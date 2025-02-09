from typing import List, Optional, Union

from schema_models.article import Article


class NewsArticle(Article):
    dateline: Optional[Union[str, List[str]]] = None
    printColumn: Optional[Union[str, List[str]]] = None
    printPage: Optional[Union[str, List[str]]] = None
    printEdition: Optional[Union[str, List[str]]] = None
    printSection: Optional[Union[str, List[str]]] = None
