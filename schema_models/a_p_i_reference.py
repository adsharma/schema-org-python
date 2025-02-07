from typing import List, Optional, Union

from schema_models.tech_article import TechArticle
from schema_models.text import Text


class APIReference(TechArticle):
    executableLibraryName: Optional[Union[Text, List[Text]]] = None
    targetPlatform: Optional[Union[Text, List[Text]]] = None
    programmingModel: Optional[Union[Text, List[Text]]] = None
    assemblyVersion: Optional[Union[Text, List[Text]]] = None
    assembly: Optional[Union[Text, List[Text]]] = None
