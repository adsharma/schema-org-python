from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.scholarly_article import ScholarlyArticle
from schema_models.text import Text


class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: Optional[Union[Text, List[Text]]] = None
