from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class AlignmentObject(Intangible):
    alignmentType: Optional[Union[str, List[str]]] = None
    targetUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    targetDescription: Optional[Union[str, List[str]]] = None
    educationalFramework: Optional[Union[str, List[str]]] = None
    targetName: Optional[Union[str, List[str]]] = None
