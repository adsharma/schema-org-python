from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.article import Article
from schema_models.text import Text


class NewsArticle(Article):
    dateline: Optional[Union[Text, List[Text]]] = None
    printColumn: Optional[Union[Text, List[Text]]] = None
    printPage: Optional[Union[Text, List[Text]]] = None
    printEdition: Optional[Union[Text, List[Text]]] = None
    printSection: Optional[Union[Text, List[Text]]] = None
