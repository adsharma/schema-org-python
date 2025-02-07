from typing import List, Optional, Union

from schema_models.scholarly_article import ScholarlyArticle
from schema_models.text import Text


class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: Optional[Union[Text, List[Text]]] = None
