from typing import List, Optional, Union

from schema_models.article import Article
from schema_models.text import Text


class Report(Article):
    reportNumber: Optional[Union[Text, List[Text]]] = None
