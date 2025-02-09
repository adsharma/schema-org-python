from typing import List, Optional, Union

from schema_models.article import Article


class TechArticle(Article):
    proficiencyLevel: Optional[Union[str, List[str]]] = None
    dependencies: Optional[Union[str, List[str]]] = None
