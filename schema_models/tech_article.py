from typing import List, Optional, Union

from schema_models.article import Article
from schema_models.text import Text


class TechArticle(Article):
    proficiencyLevel: Optional[Union[Text, List[Text]]] = None
    dependencies: Optional[Union[Text, List[Text]]] = None
