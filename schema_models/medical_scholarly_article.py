from typing import List, Optional, Union

from schema_models.scholarly_article import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: Optional[Union[str, List[str]]] = None
