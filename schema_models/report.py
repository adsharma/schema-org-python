from typing import List, Optional, Union

from schema_models.article import Article


class Report(Article):
    reportNumber: Optional[Union[str, List[str]]] = None
