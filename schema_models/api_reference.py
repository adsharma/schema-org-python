from typing import List, Optional, Union

from schema_models.tech_article import TechArticle


class APIReference(TechArticle):
    """
    Reference documentation for application programming interfaces (APIs).
    """

    executableLibraryName: Optional[Union[str, List[str]]] = None
    targetPlatform: Optional[Union[str, List[str]]] = None
    programmingModel: Optional[Union[str, List[str]]] = None
    assemblyVersion: Optional[Union[str, List[str]]] = None
    assembly: Optional[Union[str, List[str]]] = None
