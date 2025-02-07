from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.article import Article
from schema_models.text import Text


class Report(Article):
    reportNumber: Optional[Union[Text, List[Text]]] = None
